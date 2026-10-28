/* Runs Python (Pyodide) off the main thread so a slow or endless program can't freeze the page. */
importScripts('/assets/pyodide/pyodide.js');
let grader = null;
const ready = (async () => {
  const py = await loadPyodide({ indexURL: '/assets/pyodide/' });
  const src = await (await fetch('/assets/grader.py?v=20261028')).text();
  py.FS.mkdirTree('/home/pyodide');
  py.FS.writeFile('/home/pyodide/grader.py', src);
  py.runPython([
    'import sys, builtins',
    "sys.path.insert(0, '/home/pyodide')",
    'import grader',
    "def _no_input(prompt=''):",
    "    raise RuntimeError('input() does not work on this web page. Put the value straight into your code instead.')",
    'builtins.input = _no_input',
  ].join('\n'));
  grader = py.pyimport('grader');
  postMessage({ type: 'ready' });
})().catch((e) => postMessage({ type: 'fatal', error: String(e) }));

onmessage = async (e) => {
  const { id, op, code, grading } = e.data;
  try {
    await ready;
    let res;
    if (op === 'run') res = JSON.parse(await grader.run_json(code));
    else if (op === 'grade') res = JSON.parse(await grader.grade_json(code, JSON.stringify(grading)));
    else if (op === 'ping') res = {};
    postMessage({ type: 'result', id, res });
  } catch (err) {
    postMessage({ type: 'result', id, res: { stdout: '', error: String(err), ok: false, message: 'Something went wrong while running your code: ' + String(err) } });
  }
};
