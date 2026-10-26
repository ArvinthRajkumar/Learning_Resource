/* ==========================================================================
   learning_resource shared behavior. Plain JS, no dependencies, works on file://.

   Page contract (all optional, features switch on when the markup exists):
     <html data-resource="resource-id" data-page="page-id">
     <header class="topbar">                       controls get appended here
     <nav class="toc" id="toc" data-depth="3">   filled from h2 (and h3 with data-depth=3)
     <main id="main">                              searched, scroll-spied
     section[data-track][id]                       gets a "Mark as done" toggle
     pre > code.lang-py                            highlighted, gets a copy button
     .quiz[data-type][data-answer]                 interactive question
     .quiz-set[data-set] + .quiz-controls          scored set with shuffle/reset/retry
     [data-topic-stats="set"]                      per-topic accuracy table
     [data-progress-overview] [data-overall-progress] [data-weak-areas="set,set"]
     window.LR_RESOURCE (from the resource's parts.js) drives the parts menu.

   localStorage keys: "lr:<resource-id>:<key>", theme is "lr:site:theme".
   ========================================================================== */
(function () {
  "use strict";

  var doc = document;
  var root = doc.documentElement;
  var RID = root.getAttribute("data-resource") || "site";
  var PAGE = root.getAttribute("data-page") || "index";
  var RES = window.LR_RESOURCE || null;

  /* ---------- storage ---------- */
  var store = {
    key: function (k, rid) { return "lr:" + (rid || RID) + ":" + k; },
    get: function (k, fallback, rid) {
      try {
        var v = localStorage.getItem(store.key(k, rid));
        return v === null ? fallback : JSON.parse(v);
      } catch (e) { return fallback; }
    },
    set: function (k, v, rid) {
      try { localStorage.setItem(store.key(k, rid), JSON.stringify(v)); } catch (e) { /* storage blocked */ }
    },
    remove: function (k, rid) {
      try { localStorage.removeItem(store.key(k, rid)); } catch (e) { /* storage blocked */ }
    }
  };

  /* ---------- helpers ---------- */
  function $(sel, ctx) { return (ctx || doc).querySelector(sel); }
  function $$(sel, ctx) { return Array.prototype.slice.call((ctx || doc).querySelectorAll(sel)); }
  function el(tag, attrs, html) {
    var n = doc.createElement(tag);
    if (attrs) Object.keys(attrs).forEach(function (k) {
      if (k === "class") n.className = attrs[k];
      else if (k === "text") n.textContent = attrs[k];
      else n.setAttribute(k, attrs[k]);
    });
    if (html != null) n.innerHTML = html;
    return n;
  }
  function esc(s) {
    return String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;").replace(/"/g, "&quot;");
  }
  function slug(s) {
    return s.toLowerCase().replace(/[^a-z0-9]+/g, "-").replace(/^-+|-+$/g, "").slice(0, 60) || "s";
  }
  function isTyping(e) {
    var t = e.target;
    if (!t) return false;
    var tag = t.tagName;
    return tag === "INPUT" || tag === "TEXTAREA" || tag === "SELECT" || t.isContentEditable;
  }
  function shuffle(arr) {
    for (var i = arr.length - 1; i > 0; i--) {
      var j = Math.floor(Math.random() * (i + 1));
      var t = arr[i]; arr[i] = arr[j]; arr[j] = t;
    }
    return arr;
  }
  function openAncestors(node) {
    var p = node;
    while (p && p !== doc.body) {
      if (p.tagName === "DETAILS") p.open = true;
      p = p.parentNode;
    }
  }
  function flash(node) {
    node.classList.remove("flash");
    void node.offsetWidth;
    node.classList.add("flash");
  }

  var ICON = {
    search: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>',
    theme: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M12 3a9 9 0 1 0 9 9 7 7 0 0 1-9-9z"/></svg>',
    list: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M8 6h13M8 12h13M8 18h13M3 6h.01M3 12h.01M3 18h.01"/></svg>',
    parts: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg>',
    close: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M6 6l12 12M18 6 6 18"/></svg>'
  };

  /* ---------- theme ---------- */
  var THEME_KEY = "theme";
  function themeState() { return store.get(THEME_KEY, "auto", "site"); }
  function applyTheme(state) {
    if (state === "light" || state === "dark") root.setAttribute("data-theme", state);
    else root.removeAttribute("data-theme");
    var btn = $("#theme-btn");
    if (btn) {
      var label = effectiveTheme() === "dark" ? "Dark" : "Light";
      btn.setAttribute("aria-label", "Theme: " + label + ". Switch theme (t)");
      btn.title = "Theme: " + label + " (t)";
      var l = $(".label", btn);
      if (l) l.textContent = label;
    }
  }
  function effectiveTheme() {
    var st = themeState();
    if (st === "light" || st === "dark") return st;
    return window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
  }
  function cycleTheme() {
    // flip what is visible; the choice is persisted and overrides the system setting
    var next = effectiveTheme() === "dark" ? "light" : "dark";
    store.set(THEME_KEY, next, "site");
    applyTheme(next);
  }

  /* ---------- topbar controls ---------- */
  function buildTopbar() {
    var bar = $(".topbar");
    if (!bar) return;
    if (RES && RES.parts && RES.parts.length) {
      var menu = el("details", { class: "parts-menu" });
      var sum = el("summary", { class: "icon-btn", "aria-label": "All parts of this guide", title: "All parts" },
        ICON.parts + '<span class="label">Parts</span>');
      var panel = el("div", { class: "menu-panel", role: "navigation", "aria-label": "Parts" });
      var hubLink = el("a", { href: RES.hub || "index.html" }, '<span class="num">Hub</span><span>' + esc(RES.title) + "</span>");
      if (PAGE === "hub") hubLink.setAttribute("aria-current", "page");
      panel.appendChild(hubLink);
      RES.parts.forEach(function (p) {
        var a = el("a", { href: p.file });
        var prog = partProgress(p);
        a.innerHTML = '<span class="num">' + esc(p.id) + "</span><span>" + esc(p.title) + "</span>" +
          (prog.total ? '<span class="mini-done">' + prog.done + "/" + prog.total + "</span>" : "");
        if (p.id === PAGE) a.setAttribute("aria-current", "page");
        panel.appendChild(a);
      });
      menu.appendChild(sum);
      menu.appendChild(panel);
      bar.appendChild(menu);
      doc.addEventListener("click", function (e) {
        if (menu.open && !menu.contains(e.target)) menu.open = false;
      });
    }
    var sbtn = el("button", { class: "icon-btn", type: "button", id: "search-btn", "aria-label": "Search this page (/)", title: "Search (/)" },
      ICON.search + '<span class="label">Search</span>');
    sbtn.addEventListener("click", openSearch);
    bar.appendChild(sbtn);
    var tbtn = el("button", { class: "icon-btn", type: "button", id: "theme-btn" }, ICON.theme + '<span class="label">Auto</span>');
    tbtn.addEventListener("click", cycleTheme);
    bar.appendChild(tbtn);
    bar.appendChild(el("span", { class: "page-progress", id: "page-progress", "aria-hidden": "true" }));
  }

  /* ---------- TOC: build, drawer, scroll-spy ---------- */
  var tocLinks = [];
  var headings = [];
  function buildToc() {
    var main = $("#main");
    if (!main) return;
    headings = $$("h2, h3", main).filter(function (h) { return !h.closest(".quiz, .no-toc, details.recall, .card"); });
    var used = {};
    headings.forEach(function (h) {
      if (!h.id) {
        var base = slug(h.textContent), id = base, i = 2;
        while (used[id] || doc.getElementById(id)) id = base + "-" + i++;
        h.id = id;
      }
      used[h.id] = true;
    });
    var toc = $("#toc");
    if (!toc) return;
    // depth 2 by default (h2 only); <nav class="toc" data-depth="3"> also lists h3
    if (toc.getAttribute("data-depth") !== "3") headings = headings.filter(function (h) { return h.tagName === "H2"; });
    var layout = toc.closest(".layout");
    if (layout) layout.classList.add("has-toc");
    toc.innerHTML = "";
    var head = el("div", { class: "toc-head" });
    head.appendChild(el("p", { class: "toc-title", id: "toc-title" }, "On this page"));
    var close = el("button", { class: "icon-btn toc-close", type: "button", "aria-label": "Close contents" }, ICON.close);
    close.addEventListener("click", closeDrawer);
    head.appendChild(close);
    toc.appendChild(head);
    var ol = el("ol"), currentSub = null;
    headings.forEach(function (h) {
      var li = el("li");
      var a = el("a", { href: "#" + anchorFor(h) });
      a.textContent = h.getAttribute("data-toc") || h.textContent;
      a.addEventListener("click", function () { closeDrawer(); });
      li.appendChild(a);
      tocLinks.push({ a: a, h: h });
      if (h.tagName === "H2" || !ol.lastElementChild) {
        ol.appendChild(li);
        currentSub = null;
      } else {
        if (!currentSub) { currentSub = el("ol"); ol.lastElementChild.appendChild(currentSub); }
        currentSub.appendChild(li);
      }
    });
    toc.appendChild(ol);

    var fab = el("button", { class: "toc-fab", type: "button", "aria-label": "Open contents", "aria-controls": "toc", "aria-expanded": "false" },
      ICON.list + "<span>Contents</span>");
    fab.addEventListener("click", openDrawer);
    doc.body.appendChild(fab);
    var bd = el("div", { class: "toc-backdrop" });
    bd.addEventListener("click", closeDrawer);
    doc.body.appendChild(bd);
    setupScrollSpy();
  }
  function anchorFor(h) {
    // link a section's leading h2 to the section id (stable, meaningful URLs)
    var sec = h.parentElement;
    if (h.tagName === "H2" && sec && sec.tagName === "SECTION" && sec.id && sec.querySelector("h2") === h) return sec.id;
    return h.id;
  }
  function openDrawer() {
    var toc = $("#toc");
    if (!toc) return;
    toc.classList.add("open");
    $(".toc-backdrop").classList.add("show");
    $(".toc-fab").setAttribute("aria-expanded", "true");
    var active = $(".toc a.active", toc) || $(".toc a", toc);
    if (active) active.focus();
  }
  function closeDrawer() {
    var toc = $("#toc");
    if (!toc || !toc.classList.contains("open")) return;
    toc.classList.remove("open");
    $(".toc-backdrop").classList.remove("show");
    var fab = $(".toc-fab");
    fab.setAttribute("aria-expanded", "false");
  }
  var activeIdx = -1;
  function currentHeadingIndex() {
    var offset = (parseInt(getComputedStyle(root).getPropertyValue("--topbar-h"), 10) || 56) + 24;
    var idx = -1;
    for (var i = 0; i < headings.length; i++) {
      if (headings[i].getBoundingClientRect().top - offset <= 1) idx = i; else break;
    }
    return idx;
  }
  function setupScrollSpy() {
    var ticking = false;
    function update() {
      ticking = false;
      var idx = currentHeadingIndex();
      if (idx === activeIdx) return;
      activeIdx = idx;
      tocLinks.forEach(function (t, i) { t.a.classList.toggle("active", i === idx); });
      var act = tocLinks[idx];
      var toc = $("#toc");
      if (act && toc && window.innerWidth >= 1100) {
        var r = act.a.getBoundingClientRect(), tr = toc.getBoundingClientRect();
        if (r.top < tr.top + 40 || r.bottom > tr.bottom - 40) toc.scrollTop += r.top - tr.top - tr.height / 3;
      }
    }
    window.addEventListener("scroll", function () {
      if (!ticking) { ticking = true; requestAnimationFrame(update); }
    }, { passive: true });
    update();
  }
  var jumpIdx = null, jumpAt = 0;
  function jumpSection(dir) {
    var h2s = headings.filter(function (h) { return h.tagName === "H2"; });
    if (!h2s.length) return;
    var offset = (parseInt(getComputedStyle(root).getPropertyValue("--topbar-h"), 10) || 56) + 30;
    // rapid presses during smooth scrolling build on the last target, not the mid-scroll position
    var recent = jumpIdx !== null && Date.now() - jumpAt < 1000;
    var cur = -1;
    if (recent) cur = jumpIdx;
    else for (var i = 0; i < h2s.length; i++) if (h2s[i].getBoundingClientRect().top - offset <= 2) cur = i;
    var next;
    if (dir > 0) next = Math.min(cur + 1, h2s.length - 1);
    else {
      // at a section start: go to the previous one; mid-section: back to this section's start
      var atStart = recent || (cur >= 0 && h2s[cur].getBoundingClientRect().top > -40);
      next = Math.max(atStart ? cur - 1 : cur, 0);
    }
    jumpIdx = next;
    jumpAt = Date.now();
    var target = h2s[next];
    target.scrollIntoView({ block: "start" });
    if (history.replaceState) history.replaceState(null, "", "#" + anchorFor(target));
  }

  /* ---------- progress tracking ---------- */
  function partProgress(part) {
    var done = store.get("done:" + part.id, []);
    var meta = store.get("meta:" + part.id, null);
    var total = (meta && meta.total) || part.sections || 0;
    return { done: Math.min(done.length, total || done.length), total: total };
  }
  function setupProgress() {
    var sections = $$("section[data-track]");
    if (!sections.length) return;
    var done = store.get("done:" + PAGE, []);
    var ids = sections.map(function (s) { return s.id; });
    done = done.filter(function (id) { return ids.indexOf(id) !== -1; });
    store.set("meta:" + PAGE, { total: sections.length, title: doc.title });
    sections.forEach(function (s) {
      var label = el("label", { class: "done-toggle" });
      var cb = el("input", { type: "checkbox", "data-done": s.id });
      cb.checked = done.indexOf(s.id) !== -1;
      label.appendChild(cb);
      label.appendChild(doc.createTextNode(" Mark as done"));
      label.classList.toggle("is-done", cb.checked);
      cb.addEventListener("change", function () {
        var cur = store.get("done:" + PAGE, []).filter(function (x) { return x !== s.id; });
        if (cb.checked) cur.push(s.id);
        store.set("done:" + PAGE, cur);
        label.classList.toggle("is-done", cb.checked);
        renderPageProgress();
      });
      s.appendChild(label);
    });
    renderPageProgress();
  }
  function renderPageProgress() {
    var sections = $$("section[data-track]");
    var done = store.get("done:" + PAGE, []);
    var n = sections.filter(function (s) { return done.indexOf(s.id) !== -1; }).length;
    var bar = $("#page-progress");
    if (bar) bar.style.width = (sections.length ? (100 * n / sections.length) : 0) + "%";
    tocLinks.forEach(function (t) {
      var sec = t.h.closest("section[data-track]");
      var isDone = sec && t.h.tagName === "H2" && done.indexOf(sec.id) !== -1;
      var tick = $(".tick", t.a);
      if (isDone && !tick) t.a.appendChild(el("span", { class: "tick", "aria-label": "done" }, "&#10003;"));
      if (!isDone && tick) tick.remove();
    });
  }
  function renderOverview() {
    var box = $("[data-progress-overview]");
    if (box && RES) {
      box.innerHTML = "";
      RES.parts.forEach(function (p) {
        var pr = partProgress(p);
        var pct = pr.total ? Math.round(100 * pr.done / pr.total) : 0;
        var row = el("div", { class: "progress-row" });
        row.innerHTML = '<div class="pr-top"><a href="' + esc(p.file) + '">' + esc(p.id) + ". " + esc(p.title) + "</a>" +
          '<span class="pr-count">' + pr.done + " / " + pr.total + " sections</span></div>" +
          '<div class="progress' + (pct === 100 ? " ok" : "") + '" role="progressbar" aria-valuemin="0" aria-valuemax="100" aria-valuenow="' + pct +
          '" aria-label="' + esc(p.title) + ' progress"><span style="width:' + pct + '%"></span></div>';
        box.appendChild(row);
      });
    }
    var overall = $("[data-overall-progress]");
    if (overall && RES) {
      var d = 0, t = 0;
      RES.parts.forEach(function (p) { var pr = partProgress(p); d += pr.done; t += pr.total; });
      var pct = t ? Math.round(100 * d / t) : 0;
      overall.innerHTML = '<div class="progress-row"><div class="pr-top"><strong>Overall</strong><span class="pr-count">' + d + " / " + t +
        " sections (" + pct + '%)</span></div><div class="progress' + (pct === 100 ? " ok" : "") + '"><span style="width:' + pct + '%"></span></div></div>';
    }
  }

  /* ---------- code blocks: wrap, highlight, copy ---------- */
  var PY_RE = /(#[^\n]*)|("""[\s\S]*?"""|'''[\s\S]*?'''|\b[rbfuRBFU]{1,2}"(?:\\.|[^"\\\n])*"|\b[rbfuRBFU]{1,2}'(?:\\.|[^'\\\n])*'|"(?:\\.|[^"\\\n])*"|'(?:\\.|[^'\\\n])*')|\b(\d+(?:\.\d+)?(?:[eE][+-]?\d+)?)\b|\b(def|class|return|if|elif|else|for|while|in|not|and|or|is|None|True|False|import|from|as|with|try|except|finally|raise|lambda|yield|pass|break|continue|global|nonlocal|assert|del|async|await|self)\b|\b([A-Za-z_]\w*)(?=\()/g;
  function highlightPy(code) {
    var src = code.textContent, out = "", last = 0, m;
    PY_RE.lastIndex = 0;
    while ((m = PY_RE.exec(src))) {
      out += esc(src.slice(last, m.index));
      var cls = m[1] ? "com" : m[2] ? "str" : m[3] ? "num" : m[4] ? "kw" : "fn";
      out += '<span class="tok-' + cls + '">' + esc(m[0]) + "</span>";
      last = PY_RE.lastIndex;
    }
    out += esc(src.slice(last));
    code.innerHTML = out;
  }
  var SQL_KW = "select|from|where|group|by|having|order|limit|offset|join|inner|left|right|full|outer|cross|on|using|as|and|or|not|in|is|null|like|ilike|between|exists|any|all|case|when|then|else|end|union|intersect|except|distinct|insert|into|values|update|set|delete|create|table|index|unique|primary|key|foreign|references|default|check|constraint|alter|add|drop|column|view|with|recursive|over|partition|rows|range|unbounded|preceding|following|current|row|asc|desc|begin|commit|rollback|transaction|savepoint|returning|conflict|do|nothing|if|truncate|explain|analyze|trigger|before|after|for|each|replace|cast|natural|lateral|window|fetch|first|next|only|true|false";
  var SQL_RE = new RegExp("(--[^\\n]*|/\\*[\\s\\S]*?\\*/)|('(?:''|[^'])*')|\\b(\\d+(?:\\.\\d+)?)\\b|\\b(" + SQL_KW + ")\\b|\\b([A-Za-z_]\\w*)(?=\\()", "gi");
  function highlightSql(code) {
    var src = code.textContent, out = "", last = 0, m;
    SQL_RE.lastIndex = 0;
    while ((m = SQL_RE.exec(src))) {
      out += esc(src.slice(last, m.index));
      var cls = m[1] ? "com" : m[2] ? "str" : m[3] ? "num" : m[4] ? "kw" : "fn";
      out += '<span class="tok-' + cls + '">' + esc(m[0]) + "</span>";
      last = SQL_RE.lastIndex;
    }
    out += esc(src.slice(last));
    code.innerHTML = out;
  }
  function copyText(text, btn) {
    function ok() {
      btn.textContent = "Copied";
      btn.classList.add("copied");
      setTimeout(function () { btn.textContent = "Copy"; btn.classList.remove("copied"); }, 1500);
    }
    function fallback() {
      var ta = el("textarea");
      ta.value = text;
      ta.setAttribute("readonly", "");
      ta.style.position = "fixed"; ta.style.opacity = "0"; ta.style.top = "0";
      doc.body.appendChild(ta);
      ta.select();
      try { doc.execCommand("copy"); ok(); } catch (e) { btn.textContent = "Press Ctrl+C"; }
      ta.remove();
    }
    if (navigator.clipboard && window.isSecureContext) {
      navigator.clipboard.writeText(text).then(ok, fallback);
    } else fallback();
  }
  function setupCode() {
    $$("pre").forEach(function (pre) {
      if (pre.closest(".code-wrap, .formula, .no-enhance")) return;
      var code = $("code", pre) || pre;
      if (/\blang-py\b|\blanguage-python\b/.test(code.className)) highlightPy(code);
      else if (/\blang-sql\b/.test(code.className)) highlightSql(code);
      var wrap = el("div", { class: "code-wrap" });
      var head = el("div", { class: "code-head" });
      var label = code.getAttribute("data-embed") || pre.getAttribute("data-label") ||
        (/\blang-py\b|\blanguage-python\b/.test(code.className) ? "python" : /\blang-sql\b/.test(code.className) ? "sql" : "text");
      head.appendChild(el("span", { text: label }));
      var btn = el("button", { class: "copy-btn", type: "button", "aria-label": "Copy code" }, "Copy");
      btn.addEventListener("click", function () { copyText(code.textContent, btn); });
      head.appendChild(btn);
      pre.parentNode.insertBefore(wrap, pre);
      wrap.appendChild(head);
      wrap.appendChild(pre);
    });
    $$("table").forEach(function (t) {
      if (t.closest(".table-wrap")) return;
      var w = el("div", { class: "table-wrap" });
      t.parentNode.insertBefore(w, t);
      w.appendChild(t);
    });
  }

  /* ---------- quiz engine ---------- */
  function norm(s) {
    return String(s).toLowerCase().replace(/[\u2018\u2019]/g, "'").replace(/\s+/g, " ").replace(/^[\s"']+|[\s"'.,;:!]+$/g, "").trim();
  }
  function quizSetOf(q) {
    var set = q.closest("[data-set]");
    return set ? set.getAttribute("data-set") : "page-" + PAGE;
  }
  function recordResult(q, correct) {
    var setName = quizSetOf(q);
    var res = store.get("quiz:" + setName, {});
    res[q.getAttribute("data-qid")] = { c: correct ? 1 : 0, t: q.getAttribute("data-topic") || "General", ts: Date.now() };
    store.set("quiz:" + setName, res);
    doc.dispatchEvent(new CustomEvent("lr:quiz", { detail: { set: setName } }));
  }
  function setupQuiz(q, idx) {
    if (q.getAttribute("data-ready")) return;
    q.setAttribute("data-ready", "1");
    var type = q.getAttribute("data-type") || "single";
    var answer = q.getAttribute("data-answer") || "";
    if (!q.getAttribute("data-qid")) q.setAttribute("data-qid", PAGE + "-q" + idx);
    var qid = q.getAttribute("data-qid");
    var explain = $(".q-explain", q);
    if (explain) explain.hidden = true;

    // header: number, topic, type
    if (!$(".q-head", q)) {
      var typeLabel = { single: "Single choice", multi: "Select all that apply", fill: "Fill in the blank", numeric: "Numeric" }[type] || type;
      var headEl = el("div", { class: "q-head" });
      headEl.innerHTML = '<span class="q-num"></span>' +
        (q.getAttribute("data-topic") ? '<span class="tag accent">' + esc(q.getAttribute("data-topic")) + "</span>" : "") +
        '<span class="tag">' + typeLabel + "</span>" +
        (q.getAttribute("data-flag") ? '<span class="tag warn">' + esc(q.getAttribute("data-flag")) + "</span>" : "");
      q.insertBefore(headEl, q.firstChild);
    }

    var inputs = [];
    if (type === "single" || type === "multi") {
      var opts = $(".q-options", q);
      $$("li", opts).forEach(function (li) {
        var key = li.getAttribute("data-key");
        var why = $(".q-why", li);
        if (why) why.remove();
        var lab = el("label", { class: "q-opt" });
        var inp = el("input", { type: type === "single" ? "radio" : "checkbox", name: "q-" + qid, value: key });
        lab.appendChild(inp);
        lab.appendChild(el("span", { class: "q-key" }, esc(key) + "."));
        var body = el("span", { class: "q-body" });
        body.innerHTML = li.innerHTML;
        if (why) {
          var w = el("span", { class: "q-why" });
          w.innerHTML = why.innerHTML;
          body.appendChild(w);
        }
        lab.appendChild(body);
        li.innerHTML = "";
        li.appendChild(lab);
        inputs.push(inp);
      });
    } else {
      inputs = $$(".q-input", q);
      if (!inputs.length) {
        var inp = el("input", { class: "q-input", type: "text", inputmode: type === "numeric" ? "decimal" : "text", "aria-label": "Your answer", autocomplete: "off" });
        var holder = el("p");
        holder.appendChild(inp);
        if (q.getAttribute("data-unit")) holder.appendChild(doc.createTextNode(" " + q.getAttribute("data-unit")));
        q.insertBefore(holder, explain || null);
        inputs = [inp];
      }
      inputs.forEach(function (inp) {
        inp.setAttribute("autocomplete", "off");
        inp.addEventListener("keydown", function (e) { if (e.key === "Enter") { e.preventDefault(); check(); } });
      });
    }

    var actions = el("div", { class: "q-actions" });
    var checkBtn = el("button", { class: "btn small primary", type: "button" }, "Check");
    var revealBtn = el("button", { class: "btn small", type: "button" }, "Show answer");
    var retryBtn = el("button", { class: "btn small", type: "button", hidden: "" }, "Try again");
    var verdict = el("span", { class: "q-verdict", role: "status", "aria-live": "polite" });
    actions.appendChild(checkBtn); actions.appendChild(revealBtn); actions.appendChild(retryBtn); actions.appendChild(verdict);
    q.insertBefore(actions, explain || null);

    function keys() { return answer.split(",").map(function (s) { return s.trim(); }).filter(Boolean); }
    function grade() {
      if (type === "single" || type === "multi") {
        var want = keys();
        var got = inputs.filter(function (i) { return i.checked; }).map(function (i) { return i.value; });
        if (!got.length) return null;
        return want.length === got.length && want.every(function (k) { return got.indexOf(k) !== -1; });
      }
      if (type === "numeric") {
        var raw = inputs[0].value.replace(/,/g, "").trim();
        if (!raw) return null;
        var v = parseFloat(raw), target = parseFloat(answer), tol = parseFloat(q.getAttribute("data-tol") || "0");
        var good = !isNaN(v) && Math.abs(v - target) <= tol + 1e-12;
        inputs[0].classList.add(good ? "correct" : "wrong");
        return good;
      }
      // fill: blanks separated by "||", alternatives by "|"
      var blanks = answer.split("||");
      var any = inputs.some(function (i) { return i.value.trim(); });
      if (!any) return null;
      var all = true;
      inputs.forEach(function (inp, i) {
        var alts = (blanks[i] || "").split("|").map(norm);
        var ok = alts.indexOf(norm(inp.value)) !== -1;
        inp.classList.add(ok ? "correct" : "wrong");
        if (!ok) all = false;
      });
      return all;
    }
    function paintOptions() {
      if (type !== "single" && type !== "multi") return;
      var want = keys();
      inputs.forEach(function (i) {
        var lab = i.closest(".q-opt");
        var isAns = want.indexOf(i.value) !== -1;
        lab.classList.toggle("correct", isAns && i.checked);
        lab.classList.toggle("wrong", !isAns && i.checked);
        lab.classList.toggle("missed", isAns && !i.checked);
        i.disabled = true;
      });
    }
    function finish(correct, revealed) {
      q.classList.add("answered");
      paintOptions();
      inputs.forEach(function (i) { i.disabled = true; });
      if (explain) explain.hidden = false;
      checkBtn.hidden = true; revealBtn.hidden = true; retryBtn.hidden = false;
      if (revealed) {
        verdict.textContent = "Answer: " + answerText();
        verdict.className = "q-verdict";
      } else {
        verdict.textContent = correct ? "Correct" : "Not quite. Answer: " + answerText();
        verdict.className = "q-verdict " + (correct ? "ok" : "bad");
      }
      recordResult(q, !!correct && !revealed);
    }
    function answerText() {
      if (type === "fill") return answer.split("||").map(function (b) { return b.split("|")[0]; }).join(", ");
      if (type === "numeric") return answer + (q.getAttribute("data-unit") ? " " + q.getAttribute("data-unit") : "");
      return keys().join(", ");
    }
    function check() {
      var g = grade();
      if (g === null) { verdict.textContent = "Pick or type an answer first."; verdict.className = "q-verdict"; return; }
      finish(g, false);
    }
    checkBtn.addEventListener("click", check);
    revealBtn.addEventListener("click", function () { finish(false, true); });
    retryBtn.addEventListener("click", function () { resetQuiz(q); });
    q._reset = function () {
      q.classList.remove("answered");
      inputs.forEach(function (i) {
        i.disabled = false;
        if (i.type === "radio" || i.type === "checkbox") i.checked = false; else i.value = "";
        i.classList.remove("correct", "wrong");
        var lab = i.closest(".q-opt");
        if (lab) lab.classList.remove("correct", "wrong", "missed");
      });
      if (explain) explain.hidden = true;
      checkBtn.hidden = false; revealBtn.hidden = false; retryBtn.hidden = true;
      verdict.textContent = ""; verdict.className = "q-verdict";
    };
  }
  function resetQuiz(q) { if (q._reset) q._reset(); }
  function numberQuizzes(container) {
    var n = 0;
    $$(".quiz", container).forEach(function (q) {
      if (q.hidden) return;
      n++;
      var num = $(".q-num", q);
      if (num) num.textContent = "Q" + n;
    });
  }
  function setupQuizzes() {
    $$(".quiz").forEach(function (q, i) { setupQuiz(q, i + 1); });
    var sets = $$(".quiz-set");
    var looseScope = $("#main");
    if (looseScope) numberQuizzesLoose(looseScope);
    sets.forEach(setupQuizSet);
    $$("[data-topic-stats]").forEach(renderTopicStats);
    doc.addEventListener("lr:quiz", function () {
      $$("[data-topic-stats]").forEach(renderTopicStats);
      sets.forEach(updateScore);
      renderWeakAreas();
    });
  }
  function numberQuizzesLoose(scope) {
    // number standalone quizzes per section so "How this gets asked" reads Q1, Q2...
    var groups = $$("section", scope);
    if (!groups.length) groups = [scope];
    groups.forEach(function (g) {
      if (g.closest(".quiz-set")) return;
      var n = 0;
      $$(".quiz", g).forEach(function (q) {
        if (q.closest("section") !== g) return;
        n++;
        var num = $(".q-num", q);
        if (num && !num.textContent) num.textContent = "Q" + n;
      });
    });
  }
  function setupQuizSet(set) {
    var name = set.getAttribute("data-set");
    var controls = $(".quiz-controls", set);
    var list = $(".quiz-list", set) || set;
    var original = $$(".quiz", list);
    numberQuizzes(list);
    if (!controls) return;
    controls.innerHTML = "";
    function mk(label, fn, extra) {
      var b = el("button", Object.assign({ class: "btn small", type: "button" }, extra || {}), label);
      b.addEventListener("click", fn);
      controls.appendChild(b);
      return b;
    }
    mk("Shuffle questions", function () {
      shuffle($$(".quiz", list)).forEach(function (q) { list.appendChild(q); });
      numberQuizzes(list);
    });
    var shuffleOpts = mk("Shuffle options", function () {
      $$(".quiz", list).forEach(function (q) {
        var ul = $(".q-options", q);
        if (ul) shuffle($$("li", ul)).forEach(function (li) { ul.appendChild(li); });
      });
    });
    shuffleOpts.title = "Option letters stay attached to their text, so answers still match.";
    var missedBtn = mk("Retry missed only", function () {
      var res = store.get("quiz:" + name, {});
      var anyMissed = false;
      $$(".quiz", list).forEach(function (q) {
        var r = res[q.getAttribute("data-qid")];
        var missed = r && r.c === 0;
        q.hidden = !missed;
        if (missed) { anyMissed = true; resetQuiz(q); }
      });
      if (!anyMissed) {
        $$(".quiz", list).forEach(function (q) { q.hidden = false; });
        missedBtn.textContent = "No missed questions yet";
        setTimeout(function () { missedBtn.textContent = "Retry missed only"; }, 1800);
      }
      numberQuizzes(list);
      set.scrollIntoView({ block: "start" });
    });
    mk("Show all", function () {
      original.forEach(function (q) { list.appendChild(q); q.hidden = false; });
      numberQuizzes(list);
    });
    mk("Reset", function () {
      if (!window.confirm("Clear all saved answers for this quiz?")) return;
      store.remove("quiz:" + name);
      $$(".quiz", list).forEach(function (q) { q.hidden = false; resetQuiz(q); });
      numberQuizzes(list);
      doc.dispatchEvent(new CustomEvent("lr:quiz", { detail: { set: name } }));
    });
    controls.appendChild(el("span", { class: "quiz-score", "data-score": name, "aria-live": "polite" }));
    updateScore(set);
  }
  function updateScore(set) {
    var name = set.getAttribute("data-set");
    var out = $('[data-score="' + name + '"]', set);
    if (!out) return;
    var res = store.get("quiz:" + name, {});
    var total = $$(".quiz", set).length;
    var answered = 0, right = 0;
    Object.keys(res).forEach(function (k) { answered++; right += res[k].c; });
    out.textContent = "Score " + right + " / " + answered + " answered (" + total + " total)";
  }
  function topicAgg(setNames) {
    var agg = {};
    setNames.forEach(function (s) {
      var res = store.get("quiz:" + s, {});
      Object.keys(res).forEach(function (k) {
        var r = res[k];
        agg[r.t] = agg[r.t] || { right: 0, n: 0 };
        agg[r.t].n++;
        agg[r.t].right += r.c;
      });
    });
    return agg;
  }
  function renderTopicStats(box) {
    var agg = topicAgg(box.getAttribute("data-topic-stats").split(","));
    var topics = Object.keys(agg).sort();
    if (!topics.length) { box.innerHTML = '<p class="muted">Answer some questions to see per-topic accuracy.</p>'; return; }
    var rows = topics.map(function (t) {
      var a = agg[t], pct = Math.round(100 * a.right / a.n);
      return "<tr><td>" + esc(t) + '</td><td class="num">' + a.right + "/" + a.n + '</td><td class="num">' + pct +
        '%</td><td><div class="progress' + (pct >= 80 ? " ok" : "") + '"><span style="width:' + pct + '%"></span></div></td></tr>';
    }).join("");
    box.innerHTML = '<div class="table-wrap"><table class="topic-stats"><thead><tr><th>Topic</th><th class="num">Right</th><th class="num">Accuracy</th><th>Bar</th></tr></thead><tbody>' + rows + "</tbody></table></div>";
  }
  function renderWeakAreas() {
    $$("[data-weak-areas]").forEach(function (box) {
      var agg = topicAgg(box.getAttribute("data-weak-areas").split(","));
      var topics = Object.keys(agg).map(function (t) { return { t: t, pct: agg[t].right / agg[t].n, n: agg[t].n }; })
        .sort(function (a, b) { return a.pct - b.pct; });
      if (!topics.length) {
        box.innerHTML = '<p class="muted mb-0">No quiz results yet. Take the practice quiz and this box will list the topics where you missed the most.</p>';
        return;
      }
      var weak = topics.filter(function (x) { return x.pct < 0.8; });
      var link = function (t) {
        var f = RES && RES.topics && RES.topics[t];
        return f ? '<a href="' + esc(f) + '">' + esc(t) + "</a>" : esc(t);
      };
      if (!weak.length) {
        box.innerHTML = '<p class="mb-0">Every topic you attempted is at 80% or better. Retry with shuffle on, or attempt the topics you have not touched yet.</p>';
        return;
      }
      box.innerHTML = "<ul class=\"mb-0\">" + weak.map(function (x) {
        return "<li>" + link(x.t) + ": " + Math.round(100 * x.pct) + "% over " + x.n + " question" + (x.n > 1 ? "s" : "") + "</li>";
      }).join("") + "</ul>";
    });
  }

  /* ---------- search overlay (current page) ---------- */
  var searchIndex = null, searchSel = -1;
  function buildSearchIndex() {
    var main = $("#main");
    searchIndex = [];
    if (!main) return;
    var section = doc.title;
    var secId = "";
    $$("h1, h2, h3, h4, p, li, td, summary, dt, dd, figcaption, .f-body", main).forEach(function (n) {
      if (n.closest(".q-actions, .toc, .code-head")) return;
      if (/^H[1-4]$/.test(n.tagName)) { section = n.textContent.trim(); secId = n.id || secId; }
      var text = n.textContent.replace(/\s+/g, " ").trim();
      if (text.length < 2) return;
      searchIndex.push({ node: n, text: text, lower: text.toLowerCase(), section: section, secId: secId, heading: /^H[1-4]$/.test(n.tagName) });
    });
  }
  function ensureSearchUI() {
    var ov = $("#search-overlay");
    if (ov) return ov;
    ov = el("div", { class: "search-overlay", id: "search-overlay", role: "dialog", "aria-modal": "true", "aria-label": "Search this page" });
    ov.innerHTML = '<div class="search-box"><div class="sb-head"><input class="search-input" id="search-q" type="search" placeholder="Search this page" autocomplete="off" aria-label="Search query">' +
      '<button class="icon-btn" type="button" id="search-close" aria-label="Close search">' + ICON.close + '</button></div><ul class="search-results" id="search-results"></ul></div>';
    doc.body.appendChild(ov);
    ov.addEventListener("click", function (e) { if (e.target === ov) closeSearch(); });
    $("#search-close").addEventListener("click", closeSearch);
    var input = $("#search-q");
    input.addEventListener("input", function () { runSearch(input.value); });
    input.addEventListener("keydown", function (e) {
      var items = $$("#search-results a");
      if (e.key === "ArrowDown") { e.preventDefault(); searchSel = Math.min(searchSel + 1, items.length - 1); markSel(items); }
      else if (e.key === "ArrowUp") { e.preventDefault(); searchSel = Math.max(searchSel - 1, 0); markSel(items); }
      else if (e.key === "Enter") { e.preventDefault(); if (items[Math.max(searchSel, 0)]) items[Math.max(searchSel, 0)].click(); }
    });
    return ov;
  }
  function markSel(items) {
    items.forEach(function (a, i) { a.classList.toggle("sel", i === searchSel); });
    if (items[searchSel]) items[searchSel].scrollIntoView({ block: "nearest" });
  }
  function runSearch(q) {
    var out = $("#search-results");
    out.innerHTML = "";
    searchSel = -1;
    var terms = q.toLowerCase().split(/\s+/).filter(Boolean);
    if (!terms.length) return;
    if (!searchIndex) buildSearchIndex();
    var hits = [];
    searchIndex.forEach(function (it, idx) {
      var score = 0;
      for (var i = 0; i < terms.length; i++) {
        var p = it.lower.indexOf(terms[i]);
        if (p === -1) return;
        score += 1 + (it.heading ? 5 : 0) + (p === 0 ? 1 : 0);
      }
      hits.push({ it: it, score: score, idx: idx });
    });
    hits.sort(function (a, b) { return b.score - a.score || a.idx - b.idx; });
    hits = hits.slice(0, 40);
    if (!hits.length) { out.innerHTML = '<li class="search-empty">No matches on this page.</li>'; return; }
    hits.forEach(function (h) {
      var t = h.it.text, p = t.toLowerCase().indexOf(terms[0]);
      var start = Math.max(0, p - 40), snip = (start ? "..." : "") + t.slice(start, start + 140) + (t.length > start + 140 ? "..." : "");
      var html = esc(snip);
      terms.forEach(function (term) {
        var re = new RegExp("(" + term.replace(/[.*+?^${}()|[\]\\]/g, "\\$&").replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;") + ")", "gi");
        html = html.replace(re, "<mark>$1</mark>");
      });
      var a = el("a", { href: "#" + (h.it.node.id || h.it.secId) });
      a.innerHTML = '<span class="sr-sec">' + esc(h.it.section) + '</span><span class="sr-snip">' + html + "</span>";
      a.addEventListener("click", function (e) {
        e.preventDefault();
        closeSearch();
        openAncestors(h.it.node);
        h.it.node.scrollIntoView({ block: "center" });
        flash(h.it.node);
      });
      var li = el("li");
      li.appendChild(a);
      out.appendChild(li);
    });
  }
  function openSearch() {
    var target = $("[data-search-target]");
    if (target) { target.focus(); target.select && target.select(); return; }
    var ov = ensureSearchUI();
    ov.classList.add("open");
    var input = $("#search-q");
    input.focus();
    input.select();
  }
  function closeSearch() {
    var ov = $("#search-overlay");
    if (ov) ov.classList.remove("open");
  }

  /* ---------- help overlay ---------- */
  function toggleHelp() {
    var ov = $("#help-overlay");
    if (!ov) {
      ov = el("div", { class: "help-overlay", id: "help-overlay", role: "dialog", "aria-modal": "true", "aria-label": "Keyboard shortcuts" });
      ov.innerHTML = '<div class="help-box"><h2>Keyboard shortcuts</h2><dl>' +
        "<dt><kbd>/</kbd></dt><dd>Search</dd><dt><kbd>t</kbd></dt><dd>Switch light / dark</dd>" +
        "<dt><kbd>j</kbd> / <kbd>k</kbd></dt><dd>Next / previous section</dd><dt><kbd>Esc</kbd></dt><dd>Close dialogs and drawer</dd>" +
        '<dt><kbd>?</kbd></dt><dd>This help</dd></dl><p class="btn-row"><button class="btn small" type="button" id="help-close">Close</button></p></div>';
      doc.body.appendChild(ov);
      ov.addEventListener("click", function (e) { if (e.target === ov || e.target.id === "help-close") ov.classList.remove("open"); });
    }
    ov.classList.toggle("open");
  }

  /* ---------- keyboard ---------- */
  function setupKeys() {
    doc.addEventListener("keydown", function (e) {
      if (e.key === "Escape") {
        closeSearch(); closeDrawer();
        var h = $("#help-overlay"); if (h) h.classList.remove("open");
        var m = $(".parts-menu"); if (m) m.open = false;
        if (isTyping(e) && e.target.hasAttribute("data-search-target")) e.target.blur();
        return;
      }
      if (isTyping(e) || e.metaKey || e.ctrlKey || e.altKey) return;
      if (e.key === "/") { e.preventDefault(); openSearch(); }
      else if (e.key === "t") cycleTheme();
      else if (e.key === "j") jumpSection(1);
      else if (e.key === "k") jumpSection(-1);
      else if (e.key === "?") toggleHelp();
    });
  }

  /* ---------- print: expand everything ---------- */
  function setupPrint() {
    var opened = [];
    window.addEventListener("beforeprint", function () {
      opened = $$("details:not([open])");
      opened.forEach(function (d) { d.open = true; });
    });
    window.addEventListener("afterprint", function () {
      opened.forEach(function (d) { d.open = false; });
      opened = [];
    });
  }

  /* ---------- boot ---------- */
  function boot() {
    buildTopbar();
    applyTheme(themeState());
    setupCode();
    buildToc();
    setupProgress();
    setupQuizzes();
    renderOverview();
    renderWeakAreas();
    setupKeys();
    setupPrint();
    if (location.hash) {
      var t = doc.getElementById(decodeURIComponent(location.hash.slice(1)));
      if (t) { openAncestors(t); setTimeout(function () { t.scrollIntoView({ block: "start" }); }, 0); }
    }
  }

  window.LR = { store: store, openSearch: openSearch, cycleTheme: cycleTheme, partProgress: partProgress };
  if (doc.readyState === "loading") doc.addEventListener("DOMContentLoaded", boot);
  else boot();
})();
