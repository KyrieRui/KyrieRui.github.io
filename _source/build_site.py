#!/usr/bin/env python3
"""Build the English 'Python for Beginners' site (a re-creation of learn-py.org's layout)."""
import json, re, os, shutil, html, posixpath
import markdown

ROOT = '/home/claude/learnpy'
EN = '/home/claude/Python-EN/Article'
ZH = '/home/claude/src/Article'
OUT = os.environ.get('OUT', f'{ROOT}/out')
NPM = f'{ROOT}/npmtmp/node_modules'
SRC = f'{ROOT}/site_src'
VER = '20261028'

meta = json.load(open(f'{ROOT}/meta_en.json'))
meta_zh = json.load(open(f'{ROOT}/meta_zh.json'))
raw = json.load(open(f'{ROOT}/lessons_raw.json'))
EXS = json.load(open(f'{ROOT}/exercises_en.json'))
extras_zh = json.load(open(f'{ROOT}/extras.json'))

esc = lambda s: html.escape(s, quote=True)

# ---------------------------------------------------------------- lessons list
LESSONS = []
for m in meta_zh:
    ch = m['href'].split('/')[2]
    slug = m['href'].split('/')[3]
    t, d = meta['lessons'][ch]
    LESSONS.append(dict(ch=ch, slug=slug, num=m['num'], n=int(m['num']), title=t, desc=d,
                        minutes=m['minutes'], url=f'/lessons/{ch}/{slug}/', read=f'/lessons/{ch}/{slug}/read/'))
BYCH = {l['ch']: l for l in LESSONS}

# ---------------------------------------------------------------- markdown helpers
FENCE_RE = re.compile(r'^(?P<indent>[ \t]*)(?P<fence>```+|~~~+)[ \t]*(?P<info>[^\n`]*)\n(?P<body>.*?)^(?P=indent)(?P=fence)[ \t]*$', re.M | re.S)
NONSTD = re.compile(r'^\s*(?:from|import)\s+(pydantic|httpx|requests|typer|pytest|numpy|pandas|ruff|mypy|rich|click|flask|django|fastapi|attrs|aiohttp|yaml|PIL|tqdm|matplotlib|uvicorn|structlog|loguru|sqlalchemy|anthropic|openai|jinja2|bs4|toml\b|tomli)\b', re.M)

def heading_list(text):
    """Headings outside code fences: list of (line_index, level, text)."""
    out = []
    in_code = False
    fence = None
    for i, ln in enumerate(text.split('\n')):
        s = ln.strip()
        m = re.match(r'^(```+|~~~+)', s)
        if m:
            if not in_code:
                in_code, fence = True, m.group(1)
            elif s.startswith(fence):
                in_code = False
            continue
        if in_code:
            continue
        hm = re.match(r'^(#{1,6})\s+(.*?)\s*#*\s*$', ln)
        if hm:
            out.append((i, len(hm.group(1)), hm.group(2).strip()))
    return out

def python_blocks(text):
    return [m for m in FENCE_RE.finditer(text) if m.group('info').strip().split(' ')[0].lower() in ('python', 'py', 'python3')]

LANG_NAMES = {'': 'Text', 'text': 'Text', 'txt': 'Text', 'plain': 'Text', 'python': 'Python', 'py': 'Python', 'python3': 'Python',
              'bash': 'Bash', 'shell': 'Shell', 'sh': 'Shell', 'console': 'Terminal', 'toml': 'TOML', 'yaml': 'YAML', 'yml': 'YAML',
              'json': 'JSON', 'ini': 'INI', 'markdown': 'Markdown', 'md': 'Markdown', 'html': 'HTML', 'css': 'CSS', 'js': 'JavaScript',
              'javascript': 'JavaScript', 'diff': 'Diff', 'sql': 'SQL', 'cfg': 'Config', 'dockerfile': 'Dockerfile', 'pycon': 'Python console',
              'powershell': 'PowerShell', 'cmd': 'Command line', 'xml': 'XML', 'mermaid': 'Diagram', 'regex': 'Regex', 'java': 'Java', 'c': 'C'}
HLJS_LANG = {'python': 'python', 'py': 'python', 'python3': 'python', 'bash': 'bash', 'shell': 'bash', 'sh': 'bash', 'console': 'bash',
             'toml': 'ini', 'ini': 'ini', 'cfg': 'ini', 'yaml': 'yaml', 'yml': 'yaml', 'json': 'json', 'html': 'xml', 'xml': 'xml', 'css': 'css',
             'js': 'javascript', 'javascript': 'javascript', 'diff': 'diff', 'sql': 'sql', 'dockerfile': 'dockerfile', 'powershell': 'powershell',
             'pycon': 'python', 'java': 'java', 'c': 'c', 'markdown': 'markdown', 'md': 'markdown'}

USAGE = {'runnable': '· Runs on this page', 'error': '· Runs on this page (shows an error)', 'local': '· Run it on your own computer', 'output': '· Output', 'context': '· Read with the text above', 'syntax': '· Syntax only'}

class Ctx:
    def __init__(self, lesson, md_path, mode):
        self.lesson, self.md_path, self.mode = lesson, md_path, mode  # mode: 'play' | 'read'

def resolve_link(ctx, href):
    if re.match(r'^[a-z]+:', href) or href.startswith('#') or href.startswith('/'):
        return href
    path, _, frag = href.partition('#')
    base = posixpath.dirname(ctx.md_path)  # relative to Article
    target = posixpath.normpath(posixpath.join(base, path))
    if target.endswith('.md'):
        rel = target
        for l in LESSONS:
            pass
        lesson = MD_TO_LESSON.get(rel)
        if lesson:
            return (lesson['read'] if ctx.mode == 'read' else lesson['url']) + ('#' + frag if frag else '')
        if rel.startswith('examples/'):
            return '/' + posixpath.dirname(rel) + '/'
        return BYCH['python0']['url']
    return '/' + target.lstrip('/')

def code_block_html(ctx, code, info, mode):
    lang = info.strip().split(' ')[0].lower()
    name = LANG_NAMES.get(lang, lang.capitalize() if lang else 'Text')
    hl = HLJS_LANG.get(lang)
    cls = f' class="language-{hl}"' if hl else ' class="nohighlight"'
    usage = f'<span class="cb-usage">{USAGE[mode]}</span>' if mode else ''
    actions = '<button type="button" class="cb-copy" aria-label="Copy code" title="Copy the code">Copy</button>'
    if mode in ('runnable', 'error'):
        if ctx.mode == 'play':
            actions += '<button type="button" class="cb-run" title="Run this code in the browser">▶ Try it</button>'
        else:
            actions += f'<a href="{ctx.lesson["url"]}">Practise on the challenge page →</a>'
    return (f'<div class="cb not-prose" data-mode="{mode or "plain"}"><div class="cb-bar"><div class="cb-cap">'
            f'<span class="cb-dots" aria-hidden="true"><i></i><i></i><i></i></span><span class="cb-lang">{name}</span>{usage}</div>'
            f'<div class="cb-actions">{actions}</div></div>'
            f'<pre class="cb-code" tabindex="0"><code{cls}>{esc(code)}</code></pre></div>')

def render_md(ctx, text, modes=None, shift=1):
    """Markdown -> HTML with our code blocks. modes: list of modes for python blocks (in order) or None for heuristic."""
    blocks = []
    pyi = [0]
    def repl(m):
        info = m.group('info').strip()
        body = m.group('body')
        indent = m.group('indent')
        if indent:
            body = '\n'.join(l[len(indent):] if l.startswith(indent) else l for l in body.split('\n'))
        body = body.rstrip('\n')
        lang = info.split(' ')[0].lower()
        before = text[max(0, m.start() - 40):m.start()]
        skip = '<!-- skip-ci -->' in before
        mode = ''
        if lang in ('python', 'py', 'python3') and modes != 'none':
            if 'no-run' in info:
                mode = 'syntax' if ctx_is_syntax(body) else 'context'
            elif isinstance(modes, list) and pyi[0] < len(modes):
                mode = modes[pyi[0]]
                if mode in ('runnable', 'error') and (skip or NONSTD.search(body) or 'input(' in body):
                    mode = 'context'
            else:
                mode = 'context' if (skip or NONSTD.search(body) or 'input(' in body or 'threading' in body or 'multiprocessing' in body
                                     or 'open(' in body or '__file__' in body or 'os.' in body or 'subprocess' in body or 'sys.argv' in body) else 'runnable'
            pyi[0] += 1
        blocks.append(code_block_html(ctx, body, info, mode))
        return f'{indent}\n{indent}@@CB{len(blocks)-1}@@\n'
    t = text.replace('\r\n', '\n')
    t = FENCE_RE.sub(repl, t)
    t = t.replace('<!-- skip-ci -->', '')
    # heading shift
    def hshift(m):
        lvl = min(6, len(m.group(1)) + shift)
        return '#' * lvl + ' ' + m.group(2)
    t = re.sub(r'^(#{1,6})\s+(.*?)\s*#*\s*$', hshift, t, flags=re.M)
    h = markdown.markdown(t, extensions=['tables', 'sane_lists'], output_format='html')
    h = re.sub(r'<p>\s*@@CB(\d+)@@\s*</p>', lambda m: blocks[int(m.group(1))], h)
    h = re.sub(r'@@CB(\d+)@@', lambda m: blocks[int(m.group(1))], h)
    # links and images
    h = re.sub(r'(<a\s[^>]*href=")([^"]+)(")', lambda m: m.group(1) + esc(resolve_link(ctx, html.unescape(m.group(2)))) + m.group(3), h)
    def img(m):
        tag = m.group(0)
        src = re.search(r'src="([^"]+)"', tag).group(1)
        if not re.match(r'^[a-z]+:', src):
            target = posixpath.normpath(posixpath.join(posixpath.dirname(ctx.md_path), html.unescape(src)))
            MEDIA.add(target)
            tag = tag.replace(f'src="{src}"', f'src="/{target}"')
        if 'loading=' not in tag:
            tag = tag.replace('<img ', '<img loading="lazy" ')
        if '.svg' in src:
            alt = re.search(r'alt="([^"]*)"', tag)
            return f'<span class="tutorial-diagram"><span class="tutorial-diagram-scroll" role="region" tabindex="0" aria-label="{alt.group(1) if alt else "Diagram"}, scroll sideways on small screens">{tag}</span></span>'
        return tag
    h = re.sub(r'<img\s[^>]*>', img, h)
    h = h.replace('<table>', '<div class="table-wrap"><table>').replace('</table>', '</table></div>')
    return h

def ctx_is_syntax(body):
    return bool(re.search(r'[^\x00-\x7f]', body)) is False and ('...' in body or '…' in body) and len(body.split('\n')) < 8

MEDIA = set()

# md path (relative to Article) -> lesson
MD_TO_LESSON = {}
for l in LESSONS:
    for it in raw[f"/lessons/{l['ch']}/{l['slug']}/"]:
        if it['kind'] == 'step':
            f = it['file']
            m = re.match(r'\d+-original-source-(.+)\.mdx', f)
            if m:
                p = m.group(1)
                if p.startswith('codeSpecification-'):
                    rel = 'codeSpecification/' + p.split('-', 1)[1] + '.md'
                elif p == 'regex-reference':
                    rel = 'PythonBasis/python14/Common_Regular_Expressions.md'
                else:
                    c, n = p.split('-', 1)
                    rel = f'PythonBasis/{c}/{n}.md'
                MD_TO_LESSON.setdefault(rel, l)
MD_TO_LESSON['PythonBasis/python15/1.md'] = BYCH['python15']
MD_TO_LESSON['PythonBasis/python16/1.md'] = BYCH['python16']
MD_TO_LESSON['PythonBasis/python6/4.md'] = BYCH['python6']
MD_TO_LESSON['index.md'] = BYCH['python0']

def zh_rel_for(rel):
    return rel.replace('Common_Regular_Expressions', '常用的正则表达式')

# ---------------------------------------------------------------- build lesson items
def build_items(l):
    items = raw[f"/lessons/{l['ch']}/{l['slug']}/"]
    files = [it['file'] for it in items if it['kind'] == 'step']
    out = []
    # precompute segment boundaries for split files
    seg_cache = {}
    step_counter = {}
    for idx, it in enumerate(items):
        if it['kind'] == 'exercise':
            ex = EXS[f"{l['ch']}/{it['exercise']['id']}"]
            out.append(dict(kind='exercise', ex=ex))
            continue
        f = it['file']
        m = re.match(r'\d+-original-source-(.+)\.mdx', f)
        if m:
            p = m.group(1)
            if p.startswith('codeSpecification-'):
                rel = 'codeSpecification/' + p.split('-', 1)[1] + '.md'
            elif p == 'regex-reference':
                rel = 'PythonBasis/python14/Common_Regular_Expressions.md'
            else:
                c, n = p.split('-', 1)
                rel = f'PythonBasis/{c}/{n}.md'
        elif 'original-and-practice' in f:
            rel = {'python6': 'PythonBasis/python6/4.md', 'python15': 'PythonBasis/python15/1.md', 'python16': 'PythonBasis/python16/1.md'}[l['ch']]
        else:
            rel = None
        if rel is None:
            name = f.replace('.mdx', '')
            text = open(f'{ROOT}/tr/steps/{l["ch"]}__{name}.md').read()
            zh_text = extras_zh[f"/lessons/{l['ch']}/{l['slug']}/|{f}"]['content']
            out.append(dict(kind='step', md=text, rel=f'PythonBasis/{l["ch"]}/x.md', modes=it['codeModes'], zh=zh_text))
            continue
        en_text = open(f'{EN}/{rel}').read()
        zh_text = open(f'{ZH}/{zh_rel_for(rel)}').read()
        if files.count(f) == 1:
            out.append(dict(kind='step', md=en_text, rel=rel, modes=it['codeModes'], zh=zh_text))
            continue
        # split file: find this step's start heading in the Chinese source, map by index to English
        zh_heads = heading_list(zh_text)
        en_heads = heading_list(en_text)
        assert len(zh_heads) == len(en_heads), (rel, len(zh_heads), len(en_heads))
        k = step_counter.get(f, 0)
        step_counter[f] = k + 1
        out.append(dict(kind='step', rel=rel, modes=it['codeModes'], split=(f, k), head=(it['heads'][0] if it['heads'] else None), title_zh=it['title']))
    # resolve split steps
    for f in set(s['split'][0] for s in out if s.get('split')):
        steps = [s for s in out if s.get('split') and s['split'][0] == f]
        rel = steps[0]['rel']
        en_text = open(f'{EN}/{rel}').read()
        zh_text = open(f'{ZH}/{zh_rel_for(rel)}').read()
        zh_heads, en_heads = heading_list(zh_text), heading_list(en_text)
        en_lines, zh_lines = en_text.split('\n'), zh_text.split('\n')
        starts_en, starts_zh = [], []
        for j, s in enumerate(steps):
            if j == 0:
                starts_en.append(0); starts_zh.append(0); continue
            h = s['head']
            lvl = len(h) - len(h.lstrip('#'))
            txt = h.lstrip('#').strip().rstrip('#').strip()
            cand = [i for i, (ln, lv, t) in enumerate(zh_heads) if lv == lvl and t == txt and ln > starts_zh[-1]]
            if not cand:
                cand = [i for i, (ln, lv, t) in enumerate(zh_heads) if t == txt and ln > starts_zh[-1]]
            assert cand, (rel, h)
            i = cand[0]
            starts_zh.append(zh_heads[i][0]); starts_en.append(en_heads[i][0])
        for j, s in enumerate(steps):
            a = starts_en[j]; b = starts_en[j + 1] if j + 1 < len(steps) else len(en_lines)
            s['md'] = '\n'.join(en_lines[a:b])
            za = starts_zh[j]; zb = starts_zh[j + 1] if j + 1 < len(steps) else len(zh_lines)
            s['zh'] = '\n'.join(zh_lines[za:zb])
    # titles and modes check
    for s in out:
        if s['kind'] != 'step':
            continue
        hs = heading_list(s['md'])
        first_nonblank = next((ln for ln in s['md'].split('\n') if ln.strip()), '')
        if hs and s['md'].split('\n')[hs[0][0]] and s['md'].strip().startswith('#'):
            s['title'] = re.sub(r'[`*]', '', hs[0][2])
        elif hs:
            s['title'] = re.sub(r'[`*]', '', hs[0][2])
        else:
            s['title'] = l['title']
        n_zh = len(python_blocks(s['zh']))
        n_en = len(python_blocks(s['md']))
        if s['modes'] is not None and len(s['modes']) == n_zh == n_en:
            s['use_modes'] = s['modes']
        else:
            s['use_modes'] = None
            MODE_MISMATCH.append((l['ch'], s['title'], len(s['modes'] or []), n_zh, n_en))
    return out

MODE_MISMATCH = []

# ---------------------------------------------------------------- page chrome
GITHUB_SVG = '<svg viewBox="0 0 16 16" width="20" height="20" aria-hidden="true" fill="currentColor"><path d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"/></svg>'
SUN = '<svg class="ic-sun" viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>'
MOON = '<svg class="ic-moon" viewBox="0 0 24 24" width="12" height="12" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>'
ORIG = 'https://github.com/walter201230/Python'

def page(title, desc, body, extra_head='', body_attrs=''):
    return f'''<!doctype html>
<html lang="en" class="h-full">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<script>try{{if(localStorage.getItem('theme')==='light')document.documentElement.dataset.theme='light'}}catch(e){{}}</script>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700;800&family=Geist+Mono:wght@400;500;600&display=swap" rel="stylesheet">
<link rel="icon" href="/assets/favicon.svg" type="image/svg+xml">
<link rel="stylesheet" href="/assets/site.css?v={VER}">
{extra_head}
</head>
<body {body_attrs}>
<header class="site-header">
  <div class="wrap header-row">
    <a class="logo" href="/" aria-label="Python for Beginners – home"><span class="gradient-text-flow" data-text="Python for Beginners">Python for Beginners</span></a>
    <nav class="header-nav">
      <a class="nav-link" href="/about/">About</a>
      <a class="nav-icon focus-ring" href="{ORIG}" aria-label="Original tutorial on GitHub" title="Original tutorial on GitHub">{GITHUB_SVG}</a>
      <button type="button" class="theme-toggle focus-ring" aria-label="Switch theme"><span class="knob">{MOON}{SUN}</span></button>
    </nav>
  </div>
</header>
<main class="site-main">
{body}
</main>
<footer class="site-footer">
  <div class="wrap footer-row">
    <span>© 2026 Python for Beginners · English edition of the <a href="{ORIG}">walter201230/Python</a> tutorial (CC BY 4.0)</span>
    <div class="footer-links"><a href="/">Course list</a><a href="/about/">About this site</a><a href="{ORIG}">GitHub</a></div>
  </div>
</footer>
<script src="/assets/site.js?v={VER}"></script>
</body>
</html>
'''

# ---------------------------------------------------------------- home page
def ex_count(l):
    return sum(1 for it in raw[f"/lessons/{l['ch']}/{l['slug']}/"] if it['kind'] == 'exercise')

def build_home():
    groups_html = []
    for g in meta['groups']:
        cards = []
        for l in LESSONS:
            if not (g['from'] <= l['n'] <= g['to']):
                continue
            n = ex_count(l)
            if n:
                stat = f'<span class="meta-item"><span aria-hidden="true">📝</span><span><b>{n}</b> exercise{"s" if n > 1 else ""}</span></span>'
                prog = f'Progress <span data-solved>0</span> / {n}'
            else:
                stat = '<span class="meta-item"><span aria-hidden="true">📖</span><span>Concept reading</span></span>'
                prog = 'Reading chapter · no exercises'
            cards.append(f'''<article class="lesson-card" data-lesson="{l['ch']}" data-total="{n}">
  <a class="card-link" aria-label="{esc(l['title'])} – open challenge mode" href="{l['url']}"></a>
  <div class="card-top"><span class="num-badge">{l['num']}</span></div>
  <h3 class="card-title">{esc(l['title'])}</h3>
  <p class="card-desc">{esc(l['desc'])}</p>
  <div class="card-meta">{stat}<span class="dot" aria-hidden="true">·</span><span class="meta-item"><span aria-hidden="true">⏱</span><span><b>{l['minutes']}</b> min</span></span></div>
  <div class="card-foot">
    <div class="prog-row"><span>{prog}</span><span class="mono"><span data-pct>0</span>%</span></div>
    <div class="prog-bar"><div class="prog-fill gradient-tech-green" style="width:0%"></div></div>
    <div class="card-read"><a class="subtle-link focus-ring" href="{l['read']}">Read first →</a></div>
  </div>
  <div class="card-hover-bar gradient-tech-green"></div>
</article>''')
        groups_html.append(f'''<div class="group">
  <div class="group-head"><h3>{esc(g['title'])}</h3><span class="range-badge">{g['range']}</span><p>{esc(g['desc'])}</p></div>
  <div class="card-grid">{''.join(cards)}</div>
</div>''')
    body = f'''<div class="home">
<section class="hero">
  <div class="bg-tech-grid hero-grid"></div><div class="hero-glow1"></div><div class="hero-glow2"></div>
  <div class="wrap hero-inner">
    <div class="hero-cols">
      <div>
        <h1 class="hero-title gradient-text-shimmer">Python for Beginners</h1>
        <p class="hero-sub">Write code in your browser – it runs on the spot and gets checked in a second. <span class="nowrap">Get one right to unlock the next.</span></p>
        <div class="hero-ctas">
          <a class="cta gradient-tech-green focus-ring" href="{LESSONS[0]['url']}"><span>Start lesson 1</span><span class="cta-arrow">→</span></a>
          <a class="ghost-link focus-ring" href="{ORIG}">View the original tutorial on GitHub <span class="small">↗</span></a>
        </div>
      </div>
      <div class="demo" role="img" aria-label="Demo: write one line of Python, run it, pass the check and unlock the next exercise">
        <div class="demo-bar"><span class="demo-dots"><i></i><i></i><i></i></span><span class="demo-title">Exercise 1 · Say hello to Python</span></div>
        <div class="demo-body">
          <div class="d-comment"># Use print() to print one sentence</div>
          <div class="d-code"><span class="d-typed"></span><span class="d-caret"></span></div>
          <div class="d-gap"></div>
          <div class="d-run">▶ Run</div>
          <div class="d-out">Hello, Python!</div>
          <div class="d-pass">✓ Passed · next exercise unlocked</div>
        </div>
      </div>
    </div>
  </div>
</section>
<section class="wrap catalogue">
  <div class="cat-head"><div><h2>Course list</h2><p>29 chapters in three stages, each with step-by-step exercises.</p></div>
  <div class="cat-total" hidden><span data-total-solved>0</span> / 100 exercises solved</div></div>
  <div class="groups">{''.join(groups_html)}</div>
</section>
</div>'''
    return page('Python for Beginners – runs in your browser',
                'A free Python course for complete beginners: 29 chapters and 100 exercises you write, run and check right in your browser. Simple-English edition of the walter201230/Python tutorial.',
                body, body_attrs='data-page="home"')

# ---------------------------------------------------------------- lesson pages
def course_sidebar(cur, mode):
    lis = []
    for l in LESSONS:
        href = l['read'] if mode == 'read' else l['url']
        active = ' active' if l['ch'] == cur['ch'] else ''
        lis.append(f'<li><a class="course-link focus-ring{active}" href="{href}"><span class="cl-num">{l["num"]}</span><span>{esc(l["title"])}</span></a></li>')
    return f'<p class="side-label">All lessons</p><ol class="course-list">{"".join(lis)}</ol>'

def toc_items(l, items, mode):
    out = []
    si = ei = 0
    total_ex = sum(1 for i in items if i['kind'] == 'exercise')
    for idx, it in enumerate(items):
        if it['kind'] == 'step':
            si += 1
            out.append((f'step-{si-1}', f'Teaching {si:02d}', it['title'], idx))
        else:
            ei += 1
            pre = 'read-exercise-' if mode == 'read' else 'exercise-'
            out.append((pre + it['ex']['id'], f'Exercise {ei}', it['ex']['title'], idx))
    return out

def nav_block(l, mode):
    i = LESSONS.index(l)
    prev_ = LESSONS[i - 1] if i > 0 else None
    next_ = LESSONS[i + 1] if i + 1 < len(LESSONS) else None
    key = 'read' if mode == 'read' else 'url'
    a = (f'<a class="chap-nav prev focus-ring" href="{prev_[key]}"><span class="cn-label">← Previous chapter</span><span class="cn-title">{prev_["num"]} · {esc(prev_["title"])}</span></a>'
         if prev_ else '<div aria-hidden="true"></div>')
    b = (f'<a class="chap-nav next focus-ring" href="{next_[key]}"><span class="cn-label">Next chapter →</span><span class="cn-title">{next_["num"]} · {esc(next_["title"])}</span></a>'
         if next_ else '<a class="chap-nav next focus-ring" href="/"><span class="cn-label">Back to →</span><span class="cn-title">Course list</span></a>')
    return f'<nav aria-label="Chapter navigation" class="chapter-nav"><div class="cn-grid">{a}<div class="cn-mid"><span>{esc(l["title"])}</span></div>{b}</div></nav>'

def hint_html(h):
    if '\n' in h:
        first, rest = h.split('\n', 1)
        ctx = Ctx(None, '', 'play')
        return f'<li><p>{inline_md(first)}</p>{code_block_html(ctx, rest, "python", "")}</li>'
    return f'<li><p>{inline_md(h)}</p></li>'

def inline_md(s):
    h = markdown.markdown(s)
    return re.sub(r'^<p>(.*)</p>$', r'\1', h.strip(), flags=re.S)

def exercise_card_play(l, ex, k, total):
    ctx = Ctx(l, '', 'play')
    prompt = render_md(ctx, ex['prompt'], modes='none', shift=1)
    issue = f'{ORIG}/issues'
    data = {'id': ex['id'], 'lesson': l['ch'], 'starter': ex['starterCode'], 'solution': ex['solution'], 'grading': ex['grading']}
    hints = ''.join(f'<template class="hint-tpl">{hint_html(h)}</template>' for h in ex['hints'])
    return f'''<section id="exercise-{ex['id']}" class="ex-card item" data-kind="exercise" data-exercise="{ex['id']}" aria-label="Exercise {k}: {esc(ex['title'])}">
<script type="application/json" class="ex-data">{json.dumps(data, ensure_ascii=False).replace('</', '<\\/')}</script>
<header class="ex-head">
  <div class="ex-top"><span class="ex-label"><span class="pulse-dot"></span>Exercise {k} / {total}</span><span class="ex-sep" aria-hidden="true">·</span><span class="ex-title">{esc(ex['title'])}</span>
  <span class="ex-solved-badge" hidden>✓ Solved</span></div>
  <div class="prose prose-sm ex-prompt">{prompt}</div>
  <div class="ex-hints"><button type="button" class="hint-btn focus-ring">💡 Hint (<span class="hint-n">0</span> / {len(ex['hints'])})</button><ol class="hint-list"></ol>{hints}</div>
</header>
<div class="ex-editor-wrap">
  <div class="ed-bar"><div class="ed-file"><span class="dot r"></span><span class="dot y"></span><span class="dot g"></span><span class="ed-name">main.py</span></div><span class="ed-state">Editable</span></div>
  <div class="ed-host"><textarea class="ed-fallback" spellcheck="false" aria-label="Code editor">{esc(ex['starterCode'])}</textarea></div>
  <div class="ed-actions"><button type="button" class="answer-btn focus-ring">Show answer</button>
    <div class="ed-btns"><button type="button" class="btn-run focus-ring" data-action="run" title="Run (⌘/Ctrl + Enter)">▶ Run</button><button type="button" class="btn-check gradient-tech-green focus-ring" data-action="check" title="Check answer (⌘/Ctrl + Shift + Enter)">Check answer</button></div></div>
  <div class="ex-output" hidden><div class="out-label">Output</div><pre class="out-pre"></pre></div>
</div>
<div class="ex-result" role="status" aria-live="polite" hidden></div>
</section>'''

def exercise_card_read(l, ex, k, total):
    ctx = Ctx(l, '', 'read')
    prompt = render_md(ctx, ex['prompt'], modes='none', shift=1)
    return f'''<section id="read-exercise-{ex['id']}" class="rex-card" aria-label="Exercise {k}">
<header class="rex-head"><div class="rex-top"><span class="rex-badge">Exercise {k} / {total}</span><span class="rex-title">{esc(ex['title'])}</span></div>
<div class="prose prose-sm ex-prompt">{prompt}</div></header>
<a class="rex-go focus-ring" href="{l['url']}#exercise-{ex['id']}"><span class="rex-go-sub">Write it in the editor, get it checked, see the answer</span><span class="rex-go-main">Do this one on the challenge page →</span></a>
</section>'''

def build_lesson(l, mode):
    items = build_items(l)
    nsteps = sum(1 for i in items if i['kind'] == 'step')
    nex = sum(1 for i in items if i['kind'] == 'exercise')
    parts = []
    si = ei = 0
    for it in items:
        if it['kind'] == 'step':
            si += 1
            ctx = Ctx(l, it['rel'], mode)
            body = render_md(ctx, it['md'], modes=it['use_modes'], shift=1)
            cls = 'step-card item' if mode == 'play' else 'step-card read'
            parts.append(f'''<section id="step-{si-1}" class="{cls}" data-kind="step" aria-label="Teaching step {si}">
<div class="step-badge"><span class="sb-dot"></span><span class="mono">Teaching {si:02d} / {nsteps:02d}</span><span class="sb-read" hidden>· read</span></div>
<article class="prose step-prose">{body}</article></section>''')
        else:
            ei += 1
            parts.append(exercise_card_play(l, it['ex'], ei, nex) if mode == 'play' else exercise_card_read(l, it['ex'], ei, nex))
    toc = toc_items(l, items, mode)
    toc_html = ''.join(f'<li class="toc-li" data-target="{tid}"><a href="#{tid}" class="toc-link focus-ring"><span class="toc-kind">{kind}</span><span class="toc-title">{esc(t)}</span></a></li>' for tid, kind, t, _ in toc)
    if mode == 'play':
        if nex:
            sub = f'<span class="accent">{nex}</span> exercise{"s" if nex > 1 else ""}<span class="sep">·</span>about <span class="accent">{l["minutes"]}</span> min<span class="sep">·</span>solve one to unlock the next part'
        else:
            sub = f'Concept reading · about <span class="accent">{l["minutes"]}</span> min'
        head = f'''<header class="lesson-head"><h1>{esc(l['title'])}</h1><p class="lh-sub">{sub}</p>
<p class="lh-link"><a class="subtle-link focus-ring" href="{l['read']}">Read the whole chapter →</a></p></header>'''
        lock = f'<div class="lock-banner" hidden><span aria-hidden="true">🔒</span>Solve this exercise to unlock the next part ·<span class="accent lock-k">0</span><span aria-hidden="true">/</span><span>{nex}</span></div>' if nex else ''
        done = f'<div class="done-banner" hidden><div class="done-emoji" aria-hidden="true">🎉</div><p class="done-title">Chapter complete!</p><p class="done-sub">You solved all {nex} exercises in this chapter.</p></div>' if nex else ''
        end = f'<section id="lesson-end" aria-label="Chapter summary">{done}{nav_block(l, mode)}</section>'
        article = head + ''.join(parts) + lock + end
        page_attrs = f'data-page="lesson" data-lesson="{l["ch"]}" data-total="{nex}"'
    else:
        head = f'''<header class="lesson-head"><h1>{esc(l['title'])}</h1><p class="lh-sub">Full read · <span class="accent">{nsteps}</span> teaching part{"s" if nsteps > 1 else ""}{f'<span class="sep">·</span><span class="accent">{nex}</span> exercise{"s" if nex > 1 else ""}' if nex else ''}<span class="sep">·</span>about <span class="accent">{l["minutes"]}</span> min</p>
<p class="lh-note">This page is the read-through version of the chapter, with every explanation in one place. To write code and get it checked, go to <a class="accent-link focus-ring" href="{l['url']}">challenge mode</a>.</p></header>'''
        cta = f'<div class="read-cta"><p>Finished reading? Practising once is how you really learn it.</p><a class="read-cta-btn focus-ring" href="{l["url"]}">Practise in challenge mode →</a></div>' if nex else ''
        article = head + ''.join(parts) + f'<section id="lesson-end" aria-label="Chapter summary">{cta}{nav_block(l, mode)}</section>'
        page_attrs = f'data-page="read" data-lesson="{l["ch"]}" data-total="{nex}"'
    body = f'''<div class="lesson-shell bg-tech-grid">
  <div class="mobile-bar"><div class="mb-inner"><button type="button" class="dir-btn focus-ring" aria-haspopup="dialog">Contents</button></div></div>
  <div class="lesson-columns">
    <aside class="lesson-sidebar left" aria-label="All lessons">{course_sidebar(l, mode)}</aside>
    <div class="lesson-main"><article class="lesson-article">{article}</article></div>
    <aside class="lesson-sidebar right" aria-label="This chapter"><nav aria-label="This chapter's contents"><div class="side-label up">In this chapter</div><p class="toc-chapter">{esc(l['title'])}</p><ol class="toc-list">{toc_html}</ol></nav></aside>
  </div>
  <dialog class="dir-dialog" aria-labelledby="dir-title"><div class="dd-inner"><div class="dd-head"><h2 id="dir-title">Contents</h2><button type="button" class="dd-close focus-ring">Close</button></div>
  <div class="dd-tabs" aria-label="Contents scope"><button type="button" class="dd-tab focus-ring" data-tab="all" aria-pressed="true">All lessons</button><button type="button" class="dd-tab focus-ring" data-tab="chapter" aria-pressed="false">This chapter</button></div>
  <div class="dd-body"><div class="dd-pane" data-pane="all">{course_sidebar(l, mode)}</div><div class="dd-pane" data-pane="chapter" hidden><ol class="toc-list">{toc_html}</ol></div></div></div></dialog>
  <div class="py-toast" hidden><span class="spinner"></span><span class="py-toast-text">Loading Python…</span></div>
</div>'''
    extra = ''
    title = f"{l['title']} – Python for Beginners" if mode == 'play' else f"{l['title']} (full read) – Python for Beginners"
    return page(title, l['desc'], body, extra_head=extra, body_attrs=page_attrs)

def build_about():
    body = f'''<div class="lesson-shell bg-tech-grid"><div class="about wrap-narrow">
<h1>About this site</h1>
<div class="prose">
<p><strong>Python for Beginners</strong> is a simple-English edition of <a href="{ORIG}">walter201230/Python</a> (小白学 Python), a free Chinese Python tutorial by walter201230 (“Two Drops”). Its layout follows the original interactive site, <a href="https://learn-py.org/">learn-py.org</a>.</p>
<p>Every chapter has two modes:</p>
<ul><li><strong>Challenge mode</strong> – read a part, then write code in the editor. Click <em>Run</em> to see the output and <em>Check answer</em> to have it marked. Get an exercise right to unlock the next part.</li>
<li><strong>Full read</strong> – the whole chapter on one page, for reading through or looking something up.</li></ul>
<p>Your code runs in your own browser with <a href="https://pyodide.org/">Pyodide</a> (Python 3.12 compiled to WebAssembly). Nothing is sent to a server, and you don't need an account. Your progress is saved only in this browser.</p>
<h2>Licence and credits</h2>
<p>The original tutorial is © walter201230 and is shared under the <a href="https://creativecommons.org/licenses/by/4.0/">Creative Commons Attribution 4.0 (CC BY 4.0)</a> licence. This edition translates and adapts it:</p>
<ul><li>All text, code comments, exercises and diagrams were translated into simple English for young learners.</li>
<li>Example names were changed to English (for example 两点水 → “Two Drops”, 水哥 → “Brother Shui”).</li>
<li>Advertising and promotional links were removed, and a few technical mistakes were corrected.</li>
<li>Some mind-map pictures still contain Chinese text.</li></ul>
<p>Editor: <a href="https://microsoft.github.io/monaco-editor/">Monaco</a> (MIT). Syntax highlighting: <a href="https://highlightjs.org/">highlight.js</a> (BSD-3-Clause). Python runtime: <a href="https://pyodide.org/">Pyodide</a> (MPL-2.0).</p>
</div></div></div>'''
    return page('About – Python for Beginners', 'About this English edition of the walter201230/Python tutorial.', body, body_attrs='data-page="about"')

# ---------------------------------------------------------------- write everything
def main():
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    def w(path, text):
        p = os.path.join(OUT, path.lstrip('/'))
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, 'w', encoding='utf-8').write(text)
    w('index.html', build_home())
    w('about/index.html', build_about())
    for l in LESSONS:
        w(l['url'] + 'index.html', build_lesson(l, 'play'))
        w(l['read'] + 'index.html', build_lesson(l, 'read'))
    w('404.html', page('Page not found – Python for Beginners', 'Page not found',
                       '<div class="lesson-shell bg-tech-grid"><div class="about wrap-narrow"><h1>Page not found</h1><p class="muted">That page doesn\'t exist. <a class="accent-link" href="/">Back to the course list →</a></p></div></div>'))
    # assets
    A = os.path.join(OUT, 'assets'); os.makedirs(A, exist_ok=True)
    for f in ['site.css', 'site.js', 'py-worker.js', 'grader.py', 'favicon.svg']:
        shutil.copy(os.path.join(SRC, f), A)
    pyd = os.path.join(A, 'pyodide'); os.makedirs(pyd)
    for f in ['pyodide.js', 'pyodide.asm.js', 'pyodide.asm.wasm', 'python_stdlib.zip', 'pyodide-lock.json']:
        shutil.copy(f'{NPM}/pyodide/{f}', pyd)
    mon = os.path.join(A, 'monaco', 'vs'); os.makedirs(mon)
    src_vs = f'{NPM}/monaco-editor/min/vs'
    shutil.copy(f'{src_vs}/loader.js', mon)
    shutil.copytree(f'{src_vs}/base', f'{mon}/base')
    shutil.copytree(f'{src_vs}/editor', f'{mon}/editor')
    os.makedirs(f'{mon}/basic-languages')
    shutil.copytree(f'{src_vs}/basic-languages/python', f'{mon}/basic-languages/python')
    hl = os.path.join(A, 'hljs'); os.makedirs(hl)
    shutil.copy(f'{NPM}/@highlightjs/cdn-assets/highlight.min.js', hl)
    for lang in ['python', 'bash', 'ini', 'yaml', 'json', 'xml', 'css', 'javascript', 'diff', 'sql', 'dockerfile', 'powershell', 'markdown', 'java', 'c']:
        p = f'{NPM}/@highlightjs/cdn-assets/languages/{lang}.min.js'
        if os.path.exists(p):
            shutil.copy(p, hl)
    # media referenced from markdown
    for rel in sorted(MEDIA):
        s = os.path.join(EN, rel)
        if os.path.exists(s):
            d = os.path.join(OUT, rel); os.makedirs(os.path.dirname(d), exist_ok=True); shutil.copy(s, d)
        else:
            print('MISSING MEDIA', rel)
    # example files
    shutil.copytree(f'{EN}/examples', os.path.join(OUT, 'examples'), ignore=shutil.ignore_patterns('__pycache__'))
    l28 = BYCH['python28']
    ctx = Ctx(l28, 'examples/study_tracker/README.md', 'read')
    readme = open(f'{EN}/examples/study_tracker/README.md').read()
    files = '<p class="muted">Files: <a class="accent-link" href="tracker.py" download>tracker.py</a> · <a class="accent-link" href="test_tracker.py" download>test_tracker.py</a></p>'
    w('examples/study_tracker/index.html', page('Study-time tracker – Python for Beginners', 'Reference code for the final project.',
        f'<div class="lesson-shell bg-tech-grid"><div class="about wrap-narrow">{files}<div class="prose">{render_md(ctx, readme, modes="none", shift=0)}</div>'
        f'<p><a class="accent-link" href="{l28["url"]}">← Back to {esc(l28["title"])}</a></p></div></div>'))
    # Preserve the standalone tracker on tutorial rebuilds.
    fitness_src = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'fitness')
    if os.path.isdir(fitness_src):
        shutil.copytree(fitness_src, os.path.join(OUT, 'fitness'), dirs_exist_ok=True)
    open(os.path.join(OUT, '.nojekyll'), 'w').close()
    print('mode mismatches:', len(MODE_MISMATCH))
    for x in MODE_MISMATCH[:40]:
        print('  ', x)

if __name__ == '__main__':
    main()
