/* Python for Beginners – page behaviour (theme, progress, code blocks, challenge mode). */
(function () {
  'use strict';
  var doc = document, root = doc.documentElement, body = doc.body;
  var PAGE = body.dataset.page || '';
  var LESSON = body.dataset.lesson || '';

  /* ---------------- storage ---------------- */
  function load(key, def) { try { var v = localStorage.getItem(key); return v ? JSON.parse(v) : def; } catch (e) { return def; } }
  function save(key, val) { try { localStorage.setItem(key, JSON.stringify(val)); } catch (e) { /* private mode */ } }
  function progress() { return load('lp-progress', {}); }
  function lessonProgress(ch) { var p = progress()[ch] || {}; p.solved = p.solved || []; return p; }
  function setLessonProgress(ch, lp) { var p = progress(); p[ch] = lp; save('lp-progress', p); }

  /* ---------------- theme ---------------- */
  var themeBtn = doc.querySelector('.theme-toggle');
  function isLight() { return root.dataset.theme === 'light'; }
  function syncThemeLabel() { if (themeBtn) themeBtn.setAttribute('aria-label', isLight() ? 'Switch to dark theme' : 'Switch to light theme'); }
  syncThemeLabel();
  if (themeBtn) themeBtn.addEventListener('click', function () {
    if (isLight()) { delete root.dataset.theme; try { localStorage.setItem('theme', 'dark'); } catch (e) {} }
    else { root.dataset.theme = 'light'; try { localStorage.setItem('theme', 'light'); } catch (e) {} }
    syncThemeLabel();
    if (window.monaco) window.monaco.editor.setTheme(isLight() ? 'lp-light' : 'lp-dark');
  });

  /* ---------------- helpers ---------------- */
  function el(tag, cls, text) { var e = doc.createElement(tag); if (cls) e.className = cls; if (text != null) e.textContent = text; return e; }
  function escapeHtml(s) { return String(s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function inlineCode(s) { return escapeHtml(s).replace(/`([^`]+)`/g, '<code>$1</code>'); }
  function loadScript(src) {
    return new Promise(function (res, rej) { var s = doc.createElement('script'); s.src = src; s.onload = res; s.onerror = rej; doc.head.appendChild(s); });
  }

  /* ---------------- syntax highlighting + copy ---------------- */
  var blocks = doc.querySelectorAll('.cb');
  if (blocks.length) {
    loadScript('/assets/hljs/highlight.min.js').then(function () {
      var langs = ['python', 'bash', 'ini', 'yaml', 'json', 'xml', 'css', 'javascript', 'diff', 'sql', 'dockerfile', 'powershell', 'markdown', 'java', 'c'];
      var needed = {};
      doc.querySelectorAll('.cb-code code[class^="language-"]').forEach(function (c) { needed[c.className.replace('language-', '')] = 1; });
      return Promise.all(langs.filter(function (l) { return needed[l] && !window.hljs.getLanguage(l); }).map(function (l) {
        return loadScript('/assets/hljs/' + l + '.min.js').catch(function () {});
      }));
    }).then(function () {
      doc.querySelectorAll('.cb-code code[class^="language-"]').forEach(function (c) { try { window.hljs.highlightElement(c); } catch (e) {} });
    }).catch(function () {});
  }
  doc.addEventListener('click', function (e) {
    var btn = e.target.closest('.cb-copy');
    if (!btn) return;
    var code = btn.closest('.cb').querySelector('.cb-code').textContent;
    var done = function () { btn.textContent = 'Copied'; setTimeout(function () { btn.textContent = 'Copy'; }, 1500); };
    if (navigator.clipboard) navigator.clipboard.writeText(code).then(done, function () {}); else done();
  });

  /* ---------------- Python runner (Web Worker) ---------------- */
  var Py = (function () {
    var worker = null, readyP = null, seq = 0, pending = {}, toast = doc.querySelector('.py-toast');
    function showToast(text, err) {
      if (!toast) return;
      toast.hidden = false; toast.classList.toggle('err', !!err);
      toast.querySelector('.py-toast-text').textContent = text;
    }
    function start() {
      if (readyP) return readyP;
      showToast('Loading Python…');
      worker = new Worker('/assets/py-worker.js?v=20261028');
      readyP = new Promise(function (resolve, reject) {
        worker.onmessage = function (e) {
          var m = e.data;
          if (m.type === 'ready') { if (toast) toast.hidden = true; resolve(); }
          else if (m.type === 'fatal') { showToast('Python could not load. Check your internet connection and refresh the page.', true); reject(new Error(m.error)); }
          else if (m.type === 'result' && pending[m.id]) { var p = pending[m.id]; delete pending[m.id]; clearTimeout(p.timer); p.resolve(m.res); }
        };
        worker.onerror = function () { showToast('Python could not load. Refresh the page to try again.', true); reject(new Error('worker error')); };
      });
      return readyP;
    }
    function restart() {
      if (worker) worker.terminate();
      worker = null; readyP = null;
      Object.keys(pending).forEach(function (k) { clearTimeout(pending[k].timer); });
      pending = {};
      return start();
    }
    function call(op, code, grading) {
      return start().then(function () {
        return new Promise(function (resolve) {
          var id = ++seq;
          var timer = setTimeout(function () {
            delete pending[id];
            restart();
            resolve({ stdout: '', error: 'TimeoutError: your program ran for more than 10 seconds and was stopped.\nIs there a loop that never ends?', ok: false,
              message: 'Your program ran for too long and was stopped. Check for a loop that never ends.' });
          }, 10000);
          pending[id] = { resolve: resolve, timer: timer };
          worker.postMessage({ id: id, op: op, code: code, grading: grading });
        });
      });
    }
    return { start: start, run: function (code) { return call('run', code); }, grade: function (code, g) { return call('grade', code, g); } };
  })();

  function renderOutput(pre, res) {
    pre.innerHTML = '';
    if (res.stdout) pre.appendChild(doc.createTextNode(res.stdout));
    if (res.error) { var s = el('span', 'err', res.error); pre.appendChild(s); }
    if (!res.stdout && !res.error) pre.appendChild(el('span', 'muted', '(no output)'));
  }

  /* "▶ Try it" on teaching code blocks */
  doc.addEventListener('click', function (e) {
    var btn = e.target.closest('.cb-run');
    if (!btn) return;
    var cb = btn.closest('.cb');
    var code = cb.querySelector('.cb-code').textContent;
    var out = cb.querySelector('.cb-out');
    if (!out) {
      out = el('div', 'cb-out'); out.appendChild(el('div', 'cb-out-label', 'Output'));
      out.appendChild(el('pre')); cb.appendChild(out);
    }
    var pre = out.querySelector('pre');
    pre.innerHTML = '<span class="muted">Running…</span>';
    btn.disabled = true;
    Py.run(code).then(function (res) { renderOutput(pre, res); }).catch(function () {
      pre.innerHTML = '<span class="err">Python could not load. Refresh the page and try again.</span>';
    }).then(function () { btn.disabled = false; });
  });

  /* ---------------- home page ---------------- */
  if (PAGE === 'home') {
    var p = progress(), totalSolved = 0;
    doc.querySelectorAll('.lesson-card').forEach(function (card) {
      var ch = card.dataset.lesson, total = +card.dataset.total, lp = p[ch] || {};
      var solved = (lp.solved || []).length, pct;
      if (total) { pct = Math.round(100 * Math.min(solved, total) / total); totalSolved += Math.min(solved, total); card.querySelector('[data-solved]').textContent = Math.min(solved, total); }
      else pct = lp.read ? 100 : 0;
      card.querySelector('[data-pct]').textContent = pct;
      card.querySelector('.prog-fill').style.width = pct + '%';
      if (pct === 100) card.classList.add('complete');
    });
    if (totalSolved) { var ct = doc.querySelector('.cat-total'); ct.hidden = false; ct.querySelector('[data-total-solved]').textContent = totalSolved; }
    // hero demo animation
    var demo = doc.querySelector('.demo');
    if (demo) {
      var typed = demo.querySelector('.d-typed'), text = "print('Hello, Python!')";
      var reduce = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      var cycle = function () {
        demo.classList.remove('s-run', 's-out', 's-pass'); typed.textContent = '';
        if (reduce) { typed.textContent = text; demo.classList.add('s-run', 's-out', 's-pass'); return; }
        var i = 0;
        var tick = setInterval(function () {
          typed.textContent = text.slice(0, ++i);
          if (i >= text.length) {
            clearInterval(tick);
            setTimeout(function () { demo.classList.add('s-run'); }, 500);
            setTimeout(function () { demo.classList.add('s-out'); }, 1100);
            setTimeout(function () { demo.classList.add('s-pass'); }, 1700);
            setTimeout(cycle, 5200);
          }
        }, 70);
      };
      cycle();
    }
  }

  /* ---------------- lesson pages (shared) ---------------- */
  function markDoneLinks() {
    var p = progress();
    doc.querySelectorAll('.course-link').forEach(function (a) {
      var m = a.getAttribute('href').match(/\/lessons\/(python\d+)\//);
      if (!m) return;
      var lp = p[m[1]];
      a.classList.toggle('done', !!(lp && lp.complete));
    });
  }
  if (PAGE === 'lesson' || PAGE === 'read') {
    markDoneLinks();
    // contents dialog
    var dlg = doc.querySelector('.dir-dialog');
    var dirBtn = doc.querySelector('.dir-btn');
    if (dlg && dirBtn) {
      dirBtn.addEventListener('click', function () { if (dlg.showModal) dlg.showModal(); else dlg.setAttribute('open', ''); });
      dlg.querySelector('.dd-close').addEventListener('click', function () { dlg.close ? dlg.close() : dlg.removeAttribute('open'); });
      dlg.addEventListener('click', function (e) {
        if (e.target === dlg) dlg.close();
        if (e.target.closest('a')) dlg.close();
      });
      dlg.querySelectorAll('.dd-tab').forEach(function (t) {
        t.addEventListener('click', function () {
          dlg.querySelectorAll('.dd-tab').forEach(function (x) { x.setAttribute('aria-pressed', x === t ? 'true' : 'false'); });
          dlg.querySelectorAll('.dd-pane').forEach(function (pn) { pn.hidden = pn.dataset.pane !== t.dataset.tab; });
        });
      });
    }
    // reading lessons count as done once you reach the end
    var end = doc.getElementById('lesson-end');
    var totalEx = +(body.dataset.total || 0);
    if (end && 'IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (ents) {
        ents.forEach(function (en) {
          if (!en.isIntersecting) return;
          var lp = lessonProgress(LESSON);
          if (!lp.read) { lp.read = true; if (!totalEx) lp.complete = true; setLessonProgress(LESSON, lp); markDoneLinks(); }
          io.disconnect();
        });
      });
      io.observe(end);
    }
    // TOC scroll spy
    var tocLis = doc.querySelectorAll('.lesson-sidebar.right .toc-li');
    if (tocLis.length && 'IntersectionObserver' in window) {
      var map = {};
      tocLis.forEach(function (li) { map[li.dataset.target] = li; });
      var spy = new IntersectionObserver(function (ents) {
        ents.forEach(function (en) {
          if (en.isIntersecting) {
            tocLis.forEach(function (li) { li.classList.remove('current'); });
            var li = map[en.target.id]; if (li) li.classList.add('current');
          }
        });
      }, { rootMargin: '-30% 0px -60% 0px' });
      Object.keys(map).forEach(function (id) { var t = doc.getElementById(id); if (t) spy.observe(t); });
    }
  }

  /* ---------------- challenge mode ---------------- */
  if (PAGE !== 'lesson') return;
  var items = Array.prototype.slice.call(doc.querySelectorAll('.lesson-article .item'));
  var exCards = items.filter(function (it) { return it.dataset.kind === 'exercise'; });
  var lockBanner = doc.querySelector('.lock-banner'), doneBanner = doc.querySelector('.done-banner');
  var needsPython = exCards.length || doc.querySelector('.cb-run');
  if (needsPython) {
    var startPy = function () { Py.start().catch(function () {}); };
    if ('requestIdleCallback' in window) requestIdleCallback(startPy, { timeout: 1500 }); else setTimeout(startPy, 300);
  }

  function solvedSet() { return lessonProgress(LESSON).solved; }

  function applyLock(scrollToNew) {
    var solved = solvedSet();
    var firstOpen = -1;
    for (var i = 0; i < items.length; i++) {
      if (items[i].dataset.kind === 'exercise' && solved.indexOf(items[i].dataset.exercise) < 0) { firstOpen = i; break; }
    }
    var lastVisible = firstOpen < 0 ? items.length - 1 : firstOpen;
    var firstNewlyShown = null;
    // the "current" group: steps right before the open exercise (or the trailing steps when all solved)
    var groupStart = 0;
    for (var j = lastVisible; j >= 0; j--) { if (items[j].dataset.kind === 'exercise' && j !== firstOpen) { groupStart = j + 1; break; } }
    items.forEach(function (it, idx) {
      var wasHidden = it.hidden;
      it.hidden = idx > lastVisible;
      if (wasHidden && !it.hidden && !firstNewlyShown) firstNewlyShown = it;
      if (it.dataset.kind === 'step') {
        var cur = idx >= groupStart && idx <= lastVisible;
        it.classList.toggle('current', cur);
        it.classList.toggle('seen', !cur);
        it.querySelector('.sb-read').hidden = cur;
      } else {
        var isSolved = solved.indexOf(it.dataset.exercise) >= 0;
        it.classList.toggle('solved', isSolved);
        it.classList.toggle('current', idx === firstOpen);
        it.querySelector('.ex-solved-badge').hidden = !isSolved;
        if (!it.hidden) ensureEditor(it);
      }
    });
    var nSolved = exCards.filter(function (c) { return solved.indexOf(c.dataset.exercise) >= 0; }).length;
    if (lockBanner) { lockBanner.hidden = firstOpen < 0; lockBanner.querySelector('.lock-k').textContent = nSolved; }
    if (doneBanner) doneBanner.hidden = firstOpen >= 0;
    // table of contents
    doc.querySelectorAll('.toc-li').forEach(function (li) {
      var t = doc.getElementById(li.dataset.target);
      if (!t) return;
      li.classList.toggle('locked', t.hidden);
      li.classList.toggle('solved', t.dataset.kind === 'exercise' && solved.indexOf(t.dataset.exercise) >= 0);
    });
    var lp = lessonProgress(LESSON);
    var complete = exCards.length ? firstOpen < 0 : !!lp.read;
    if (lp.complete !== complete) { lp.complete = complete; setLessonProgress(LESSON, lp); markDoneLinks(); }
    if (scrollToNew && firstNewlyShown) setTimeout(function () { firstNewlyShown.scrollIntoView({ behavior: 'smooth', block: 'start' }); }, 700);
  }

  /* ---- editors (Monaco, with a textarea fallback) ---- */
  var monacoP = null;
  function getMonaco() {
    if (monacoP) return monacoP;
    monacoP = loadScript('/assets/monaco/vs/loader.js').then(function () {
      return new Promise(function (resolve, reject) {
        window.MonacoEnvironment = { getWorkerUrl: function () { return '/assets/monaco/vs/base/worker/workerMain.js'; } };
        window.require.config({ paths: { vs: '/assets/monaco/vs' } });
        window.require(['vs/editor/editor.main'], function () {
          var m = window.monaco;
          m.editor.defineTheme('lp-dark', { base: 'vs-dark', inherit: true, rules: [], colors: { 'editor.background': '#0f172b', 'editorGutter.background': '#0f172b', 'editor.lineHighlightBackground': '#1d293d80', 'editorLineNumber.foreground': '#45556c', 'editorLineNumber.activeForeground': '#cad5e2' } });
          m.editor.defineTheme('lp-light', { base: 'vs', inherit: true, rules: [], colors: { 'editor.background': '#ffffff', 'editor.lineHighlightBackground': '#f1f5f9' } });
          resolve(m);
        }, reject);
      });
    });
    return monacoP;
  }

  function draftKey(card) { return 'lp-code:' + LESSON + '/' + card.dataset.exercise; }
  function exData(card) { if (!card._data) card._data = JSON.parse(card.querySelector('.ex-data').textContent); return card._data; }

  function ensureEditor(card) {
    if (card._ed) return;
    var data = exData(card);
    var ta = card.querySelector('.ed-fallback');
    var draft = null; try { draft = localStorage.getItem(draftKey(card)); } catch (e) {}
    ta.value = draft != null ? draft : data.starter;
    var api = {
      get: function () { return ta.value; },
      set: function (v) { ta.value = v; saveDraft(); },
      focus: function () { ta.focus(); }
    };
    function saveDraft() { try { localStorage.setItem(draftKey(card), api.get()); } catch (e) {} }
    ta.addEventListener('input', saveDraft);
    ta.addEventListener('keydown', function (e) {
      if (e.key === 'Tab' && !e.shiftKey) { e.preventDefault(); var s = ta.selectionStart; ta.setRangeText('    ', s, ta.selectionEnd, 'end'); saveDraft(); }
      if (e.key === 'Enter' && (e.metaKey || e.ctrlKey)) { e.preventDefault(); (e.shiftKey ? check : run)(card); }
    });
    card._ed = api;
    // upgrade to Monaco when the card is near the screen
    var upgrade = function () {
      getMonaco().then(function (m) {
        var host = card.querySelector('.ed-host');
        var ed = m.editor.create(host, {
          value: ta.value, language: 'python', theme: isLight() ? 'lp-light' : 'lp-dark', automaticLayout: true,
          minimap: { enabled: false }, scrollBeyondLastLine: false, fontSize: 14, lineHeight: 21,
          fontFamily: 'Menlo, Monaco, "Courier New", monospace', padding: { top: 12, bottom: 12 }, tabSize: 4, insertSpaces: true,
          quickSuggestions: false, suggestOnTriggerCharacters: false, wordBasedSuggestions: 'off', parameterHints: { enabled: false },
          renderLineHighlight: 'line', overviewRulerLanes: 0, hideCursorInOverviewRuler: true, scrollbar: { alwaysConsumeMouseWheel: false },
          fixedOverflowWidgets: true
        });
        ta.hidden = true;
        api.get = function () { return ed.getValue(); };
        api.set = function (v) { ed.setValue(v); saveDraft(); };
        api.focus = function () { ed.focus(); };
        ed.onDidChangeModelContent(saveDraft);
        ed.addCommand(m.KeyMod.CtrlCmd | m.KeyCode.Enter, function () { run(card); });
        ed.addCommand(m.KeyMod.CtrlCmd | m.KeyMod.Shift | m.KeyCode.Enter, function () { check(card); });
      }).catch(function () { /* keep the textarea */ });
    };
    if ('IntersectionObserver' in window) {
      var io = new IntersectionObserver(function (ents) { if (ents.some(function (en) { return en.isIntersecting; })) { io.disconnect(); upgrade(); } }, { rootMargin: '600px 0px' });
      io.observe(card);
    } else upgrade();
    bindCard(card);
  }

  function setBusy(card, busy) {
    card.querySelectorAll('.btn-run,.btn-check').forEach(function (b) { b.disabled = busy; });
  }
  function showOutput(card, res) {
    var box = card.querySelector('.ex-output');
    box.hidden = false;
    renderOutput(box.querySelector('.out-pre'), res);
  }
  function run(card) {
    var code = card._ed.get();
    setBusy(card, true);
    var box = card.querySelector('.ex-output'); box.hidden = false;
    box.querySelector('.out-pre').innerHTML = '<span class="muted">Running…</span>';
    Py.run(code).then(function (res) { showOutput(card, res); }).catch(function () {
      box.querySelector('.out-pre').innerHTML = '<span class="err">Python could not load. Refresh the page and try again.</span>';
    }).then(function () { setBusy(card, false); });
  }
  function check(card) {
    var code = card._ed.get(), data = exData(card);
    setBusy(card, true);
    var resBox = card.querySelector('.ex-result');
    Py.grade(code, data.grading).then(function (res) {
      showOutput(card, res);
      resBox.hidden = false;
      resBox.className = 'ex-result ' + (res.ok ? 'pass' : 'fail');
      resBox.innerHTML = '<div class="res-head"><span class="res-icon" aria-hidden="true">' + (res.ok ? '✓' : '✗') + '</span><span class="res-title">' +
        (res.ok ? 'Passed!' : 'Not yet') + '</span></div><p class="res-msg">' + inlineCode(res.ok ? (nextText(card)) : res.message) + '</p>';
      if (res.ok) {
        var lp = lessonProgress(LESSON);
        var first = lp.solved.indexOf(data.id) < 0;
        if (first) { lp.solved.push(data.id); setLessonProgress(LESSON, lp); confetti(); }
        applyLock(first);
      }
    }).catch(function () {
      resBox.hidden = false; resBox.className = 'ex-result fail';
      resBox.innerHTML = '<div class="res-head"><span class="res-icon">✗</span><span class="res-title">Python could not load</span></div><p class="res-msg">Check your internet connection and refresh the page.</p>';
    }).then(function () { setBusy(card, false); });
  }
  function nextText(card) {
    var idx = exCards.indexOf(card);
    if (idx === exCards.length - 1) return 'Great work – that was the last exercise in this chapter.';
    return 'Great work – the next part is now unlocked below.';
  }
  function bindCard(card) {
    if (card._bound) return; card._bound = true;
    var data = exData(card);
    card.querySelector('.btn-run').addEventListener('click', function () { run(card); });
    card.querySelector('.btn-check').addEventListener('click', function () { check(card); });
    var hb = card.querySelector('.hint-btn'), list = card.querySelector('.hint-list'), tpls = card.querySelectorAll('.hint-tpl'), shown = 0;
    hb.addEventListener('click', function () {
      if (shown >= tpls.length) return;
      list.appendChild(tpls[shown].content.cloneNode(true));
      shown++;
      card.querySelector('.hint-n').textContent = shown;
      if (shown >= tpls.length) hb.disabled = true;
      if (window.hljs) list.querySelectorAll('.cb-code code.language-python:not(.hljs)').forEach(function (c) { window.hljs.highlightElement(c); });
    });
    var ab = card.querySelector('.answer-btn'), armed = null;
    ab.addEventListener('click', function () {
      if (!armed) {
        ab.classList.add('confirm'); ab.textContent = 'Click again to replace your code with the answer';
        armed = setTimeout(function () { armed = null; ab.classList.remove('confirm'); ab.textContent = 'Show answer'; }, 3500);
        return;
      }
      clearTimeout(armed); armed = null; ab.classList.remove('confirm'); ab.textContent = 'Show answer';
      card._ed.set(data.solution);
      card._ed.focus();
    });
  }

  function confetti() {
    if (window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
    var colors = ['#00d294', '#00d3bd', '#00d2ef', '#a4f4cf', '#fcbb00'];
    for (var i = 0; i < 36; i++) {
      var c = el('span', 'confetti');
      c.style.left = Math.random() * 100 + 'vw';
      c.style.background = colors[i % colors.length];
      c.style.animationDuration = (1.6 + Math.random() * 1.4) + 's';
      c.style.animationDelay = (Math.random() * 0.3) + 's';
      body.appendChild(c);
      setTimeout(function (n) { return function () { n.remove(); }; }(c), 3500);
    }
  }

  applyLock(false);
  // jump to a requested exercise if it's unlocked
  if (location.hash) { var t = doc.querySelector(location.hash); if (t && !t.hidden) setTimeout(function () { t.scrollIntoView(); }, 50); }
})();
