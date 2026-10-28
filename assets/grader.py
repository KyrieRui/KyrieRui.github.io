# Runs learner code and checks it. Used in the browser (Pyodide worker) and for build-time validation.
import ast, io, sys, traceback, json, math, contextlib

class _AsyncioRunToAwait(ast.NodeTransformer):
    """Turn module-level asyncio.run(x) into `await x` so it works inside the browser's event loop."""
    def __init__(self):
        self.depth = 0
    def _scope(self, node):
        self.depth += 1
        self.generic_visit(node)
        self.depth -= 1
        return node
    visit_FunctionDef = visit_AsyncFunctionDef = visit_Lambda = visit_ClassDef = _scope
    def visit_Call(self, node):
        self.generic_visit(node)
        f = node.func
        if (self.depth == 0 and isinstance(f, ast.Attribute) and f.attr == 'run'
                and isinstance(f.value, ast.Name) and f.value.id == 'asyncio' and node.args):
            return ast.copy_location(ast.Await(node.args[0]), node)
        return node

def _clean_tb(exc):
    lines = traceback.format_exception(type(exc), exc, exc.__traceback__)
    out = []
    keep = False
    for ln in lines:
        if ln.startswith('Traceback'):
            out.append(ln); continue
        if 'File "<exec>"' in ln or 'File "main.py"' in ln:
            keep = True
        if keep or not ln.startswith('  File'):
            if ln.startswith('  File') and 'main.py' not in ln:
                continue
            out.append(ln)
    return ''.join(out)

async def run_code(code, glb=None):
    """Return (stdout, error_text or None, globals)."""
    g = {'__name__': '__main__'} if glb is None else glb
    buf = io.StringIO()
    err = None
    try:
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', SyntaxWarning)
            tree = ast.parse(code, 'main.py', 'exec')
        tree = ast.fix_missing_locations(_AsyncioRunToAwait().visit(tree))
        import warnings
        with warnings.catch_warnings():
            warnings.simplefilter('ignore', SyntaxWarning)
            compiled = compile(tree, 'main.py', 'exec', flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT)
        with contextlib.redirect_stdout(buf), contextlib.redirect_stderr(buf):
            import logging
            for h in list(logging.root.handlers):
                logging.root.removeHandler(h)
            res = eval(compiled, g)
            if res is not None and hasattr(res, '__await__'):
                await res
    except SystemExit:
        pass
    except BaseException as e:  # noqa
        err = _clean_tb(e)
    return buf.getvalue(), err, g

def _norm(v):
    if isinstance(v, (set, frozenset)):
        try: return sorted(_norm(x) for x in v)
        except TypeError: return [_norm(x) for x in v]
    if isinstance(v, (list, tuple)):
        return [_norm(x) for x in v]
    if isinstance(v, dict):
        return {str(k): _norm(x) for k, x in v.items()}
    return v

def _eq(a, b):
    if isinstance(a, bool) or isinstance(b, bool):
        return a is b if isinstance(a, bool) and isinstance(b, bool) else False
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return math.isclose(a, b, rel_tol=1e-9, abs_tol=1e-9)
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(_eq(x, y) for x, y in zip(a, b))
    if isinstance(a, dict) and isinstance(b, dict):
        return a.keys() == b.keys() and all(_eq(a[k], b[k]) for k in a)
    return a == b

def _ast_has(tree, spec):
    kind, _, name = spec.partition(':')
    for node in ast.walk(tree):
        if type(node).__name__ != kind:
            continue
        if not name:
            return True
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)) and node.name == name:
            return True
        if isinstance(node, ast.Assign):
            for t in node.targets:
                for n in ast.walk(t):
                    if isinstance(n, ast.Name) and n.id == name:
                        return True
        if isinstance(node, (ast.Import, ast.ImportFrom)):
            if any(a.name == name or a.name.split('.')[0] == name or a.asname == name for a in node.names):
                return True
            if isinstance(node, ast.ImportFrom) and node.module == name:
                return True
    return False

AST_LABELS = {
    'FunctionDef': 'a function definition (def)', 'AsyncFunctionDef': 'an async function (async def)',
    'ClassDef': 'a class definition (class)', 'For': 'a for loop', 'While': 'a while loop', 'If': 'an if statement',
    'Import': 'an import statement', 'ImportFrom': 'a from ... import statement', 'Assign': 'an assignment',
    'Try': 'a try statement', 'With': 'a with statement', 'JoinedStr': 'an f-string', 'FormattedValue': 'an f-string {placeholder}',
    'ListComp': 'a list comprehension', 'DictComp': 'a dict comprehension', 'Nonlocal': 'a nonlocal statement',
    'Raise': 'a raise statement', 'Tuple': 'a tuple', 'BoolOp': 'and / or', 'Match': 'a match statement',
    'Continue': 'continue', 'Lambda': 'a lambda', 'Yield': 'yield',
}

def _describe(spec):
    kind, _, name = spec.partition(':')
    label = AST_LABELS.get(kind, kind)
    return f'{label} for `{name}`' if name else label

def _show(s):
    return s.replace('\n', '\\n')

def _compare_stdout(expected, actual):
    def norm(s):
        lines = [ln.rstrip() for ln in s.replace('\r\n', '\n').split('\n')]
        while lines and lines[-1] == '':
            lines.pop()
        return lines
    e, a = norm(expected), norm(actual)
    if e == a:
        return None
    if not a:
        return f"Your program didn't print anything. Expected `{_show(expected)}`."
    for i, (x, y) in enumerate(zip(e, a)):
        if x != y:
            extra = ''
            if x.replace(' ', '') == y.replace(' ', ''):
                extra = ' (only the spaces are different)'
            elif x.lower() == y.lower():
                extra = ' (only upper/lower case is different)'
            return f"Line {i + 1} is different{extra}. Expected `{x}`, but got `{y}`."
    if len(a) < len(e):
        return f"Your output is missing lines. The next expected line is `{e[len(a)]}`."
    return f"Your output has extra lines, starting with `{a[len(e)]}`."

async def grade(code, grading):
    """Return dict(ok, stdout, error, message)."""
    out, err, g = await run_code(code)
    res = {'ok': False, 'stdout': out, 'error': err, 'message': ''}
    if err:
        last = err.strip().splitlines()[-1] if err.strip() else 'Error'
        res['message'] = f'Your code raised an error: `{last}`. Read the red message in the output and fix that line first.'
        return res
    try:
        tree = ast.parse(code)
    except SyntaxError:
        tree = ast.parse('')
    for spec in grading.get('requiredAst', []):
        if not _ast_has(tree, spec):
            res['message'] = f'The output may be right, but this exercise asks you to use {_describe(spec)}.'
            return res
    if 'stdoutEquals' in grading:
        msg = _compare_stdout(grading['stdoutEquals'], out)
        if msg:
            res['message'] = 'The output is not what was expected. ' + msg
            return res
    for name, want in grading.get('varsEqual', {}).items():
        if name not in g:
            res['message'] = f'The output looks right, but the variable `{name}` is missing. Did you assign it?'
            return res
        if not _eq(_norm(g[name]), _norm(want)):
            res['message'] = f'The variable `{name}` has the wrong value. Expected `{json.dumps(want, ensure_ascii=False)}`, but it is `{repr(g[name])}`.'
            return res
    res['ok'] = True
    res['message'] = 'Your output matches and the checks passed.'
    return res

async def run_json(code):
    out, err, _ = await run_code(code)
    return json.dumps({'stdout': out, 'error': err})

async def grade_json(code, grading_json):
    res = await grade(code, json.loads(grading_json))
    return json.dumps(res)
