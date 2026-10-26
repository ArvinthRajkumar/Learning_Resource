/* Interactive visualisers for the DSA Master Guide.
   Each <div class="viz-slot" data-viz="key"> on a page is filled in when it scrolls near the viewport.
   Keys look like "name" or "name:variant"; see VIZ[...] below. No network access, no dependencies. */
(function () {
'use strict';
/* ====================== tiny DOM helpers ====================== */
function h(tag, props, ...kids) {
  const el = document.createElement(tag);
  if (props) for (const k in props) {
    const v = props[k];
    if (v === undefined || v === null || v === false) continue;
    if (k === 'class') el.className = v;
    else if (k === 'text') el.textContent = v;
    else if (k === 'html') el.innerHTML = v;
    else if (k.slice(0, 2) === 'on') el.addEventListener(k.slice(2), v);
    else if (k === 'value') el.value = v;
    else el.setAttribute(k, v === true ? '' : v);
  }
  const add = (c) => {
    if (c === null || c === undefined || c === false) return;
    if (Array.isArray(c)) c.forEach(add);
    else el.appendChild(c.nodeType ? c : document.createTextNode(String(c)));
  };
  kids.forEach(add);
  return el;
}
const SVGNS = 'http://www.w3.org/2000/svg';
function s(tag, attrs, ...kids) {
  const el = document.createElementNS(SVGNS, tag);
  if (attrs) for (const k in attrs) el.setAttribute(k, attrs[k]);
  kids.forEach((c) => { if (c !== null && c !== undefined) el.appendChild(c.nodeType ? c : document.createTextNode(String(c))); });
  return el;
}
function esc(t) { return String(t).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;'); }

/* ====================== input parsing ====================== */
function parseNums(str, opts) {
  opts = opts || {};
  const max = opts.max || 16;
  const a = String(str).split(/[\s,]+/).filter(Boolean).map(Number);
  if (!a.length || a.some((x) => !Number.isFinite(x))) throw new Error('Please enter numbers separated by commas, e.g. 4, 2, 7');
  if (a.length > max) throw new Error('Please use at most ' + max + ' values so the animation stays readable.');
  if (opts.int && a.some((x) => !Number.isInteger(x))) throw new Error('Please use whole numbers.');
  if (opts.min !== undefined && a.some((x) => x < opts.min)) throw new Error('Values must be at least ' + opts.min + '.');
  return opts.sort ? a.slice().sort((x, y) => x - y) : a;
}
function parseStr(str, max) {
  const t = String(str);
  if (!t.length) throw new Error('Please enter some text.');
  if (t.length > (max || 20)) throw new Error('Please use at most ' + (max || 20) + ' characters.');
  return t;
}
function mk(items, marks, tags) { // helper to build cell items
  return items.map((v, i) => ({ v: v, cls: (marks && marks[i]) || '', tag: (tags && tags[i]) || '' }));
}
function cellsRow(label, arr, marks, tags, noIdx) {
  return { kind: 'cells', label: label, items: mk(arr, marks, tags), idx: !noIdx };
}
function barsRow(arr, marks) { return { kind: 'bars', items: mk(arr, marks) }; }
function stackRow(label, arr, topCls) {
  return { kind: 'stack', label: label, items: arr.map((v, i) => ({ v: v, cls: i === arr.length - 1 ? (topCls || 'hl') : '' })) };
}
function kvRow(label, pairs) { return { kind: 'kv', label: label, items: pairs }; }
function range(a, b) { const r = []; for (let i = a; i <= b; i++) r.push(i); return r; }
function layoutCircle(n, w, hh, r) {
  const cx = w / 2, cy = hh / 2, R = r || Math.min(w, hh) / 2 - 36;
  return range(0, n - 1).map((i) => {
    const ang = -Math.PI / 2 + (2 * Math.PI * i) / n;
    return { x: cx + R * Math.cos(ang), y: cy + R * Math.sin(ang) };
  });
}

/* ====================== frame renderers ====================== */
function renderRow(r) {
  const wrap = h('div', { class: 'row' });
  if (r.label) wrap.appendChild(h('div', { class: 'rl', text: r.label }));
  if (r.kind === 'cells') {
    const c = h('div', { class: 'cells' });
    r.items.forEach((it, i) => {
      c.appendChild(h('div', { class: 'cellbox' },
        h('div', { class: 'cell ' + (it.cls || ''), text: String(it.v) }),
        h('div', { class: 'tag', text: it.tag || '' }),
        r.idx ? h('div', { class: 'idx', text: '[' + i + ']' }) : null));
    });
    if (!r.items.length) c.appendChild(h('div', { class: 'cell empty', text: '·' }));
    wrap.appendChild(c);
  } else if (r.kind === 'bars') {
    const max = Math.max(1, ...r.items.map((x) => Math.abs(x.v)));
    const c = h('div', { class: 'bars' });
    r.items.forEach((it) => {
      const bar = h('div', { class: 'bar ' + (it.cls || ''), text: String(it.v) });
      bar.style.height = Math.max(8, (Math.abs(it.v) / max) * 100) + '%';
      c.appendChild(bar);
    });
    wrap.appendChild(c);
  } else if (r.kind === 'stack') {
    const c = h('div', { class: 'stackcol' });
    r.items.forEach((it) => c.appendChild(h('div', { class: 'cell ' + (it.cls || ''), text: String(it.v) })));
    if (!r.items.length) c.appendChild(h('div', { class: 'tip', text: '(empty)' }));
    wrap.appendChild(c);
  } else if (r.kind === 'kv') {
    const c = h('div', { class: 'kv' });
    r.items.forEach((it) => c.appendChild(h('span', { class: it.cls || '', text: it.k !== undefined ? it.k + ': ' + it.v : String(it.v) })));
    if (!r.items.length) c.appendChild(h('span', { text: '(empty)' }));
    wrap.appendChild(c);
  }
  return wrap;
}
function renderSvg(sv) {
  const svg = s('svg', { viewBox: '0 0 ' + sv.w + ' ' + sv.h, width: Math.min(sv.w, 760), height: sv.h * Math.min(1, 760 / sv.w), role: 'img', 'aria-label': sv.label || 'diagram' });
  const N = sv.nodes, R = sv.r || 20;
  (sv.edges || []).forEach((e) => {
    const a = N[e.a], b = N[e.b];
    if (!a || !b) return;
    let x1 = a.x, y1 = a.y, x2 = b.x, y2 = b.y;
    const dx = x2 - x1, dy = y2 - y1, len = Math.hypot(dx, dy) || 1;
    if (e.dir) { x2 -= (dx / len) * (R + 4); y2 -= (dy / len) * (R + 4); }
    svg.appendChild(s('line', { x1: x1, y1: y1, x2: x2, y2: y2, class: 'edge ' + (e.cls || '') }));
    if (e.dir) {
      const ux = dx / len, uy = dy / len, px = -uy, py = ux;
      svg.appendChild(s('polygon', { points: [x2, y2, x2 - ux * 10 + px * 5, y2 - uy * 10 + py * 5, x2 - ux * 10 - px * 5, y2 - uy * 10 - py * 5].join(','), fill: e.cls === 'on' ? 'var(--accent)' : 'var(--dim)' }));
    }
    if (e.label !== undefined && e.label !== '') {
      svg.appendChild(s('text', { x: (a.x + b.x) / 2 + (-dy / len) * 10, y: (a.y + b.y) / 2 + (dx / len) * 10, class: 'elabel', 'text-anchor': 'middle' }, String(e.label)));
    }
  });
  N.forEach((n) => {
    if (n.hidden) return;
    const g = s('g', { class: 'node ' + (n.cls || '') });
    g.appendChild(s('circle', { cx: n.x, cy: n.y, r: R }));
    g.appendChild(s('text', { x: n.x, y: n.y }, String(n.label)));
    if (n.sub !== undefined && n.sub !== '') g.appendChild(s('text', { x: n.x, y: n.y - R - 6, class: 'sub' }, String(n.sub)));
    svg.appendChild(g);
  });
  return h('div', { class: 'svgwrap' }, svg);
}
function renderTable(t) {
  const tb = h('table', { class: 'grid-t' });
  if (t.head) {
    const tr = h('tr');
    if (t.corner !== undefined) tr.appendChild(h('td', null, h('div', { class: 'gcell hd', text: t.corner })));
    t.head.forEach((x) => tr.appendChild(h('td', null, h('div', { class: 'gcell hd', text: String(x) }))));
    tb.appendChild(tr);
  }
  t.rows.forEach((row, ri) => {
    const tr = h('tr');
    if (t.side) tr.appendChild(h('td', null, h('div', { class: 'gcell hd', text: String(t.side[ri]) })));
    row.forEach((c) => {
      const o = typeof c === 'object' && c !== null ? c : { v: c };
      tr.appendChild(h('td', null, h('div', { class: 'gcell ' + (o.cls || ''), text: o.v === undefined || o.v === null ? '' : String(o.v) })));
    });
    tb.appendChild(tr);
  });
  return h('div', { class: 'svgwrap', style: 'overflow:auto' }, tb);
}
function renderGantt(g) {
  const max = Math.max(...g.items.map((i) => i.e), 1) + 1;
  const wrap = h('div', { class: 'row', style: 'position:relative' });
  if (g.label) wrap.appendChild(h('div', { class: 'rl', text: g.label }));
  g.items.forEach((it) => {
    const lane = h('div', { style: 'position:relative;height:26px;margin:3px 0;background:var(--panel2);border-radius:6px' });
    const bar = h('div', { class: 'bar ' + (it.cls || ''), text: it.label || '', style: 'position:absolute;top:0;height:100%;max-width:none;min-width:0;border-radius:6px;align-items:center;left:' + (it.s / max) * 100 + '%;width:' + Math.max(((it.e - it.s) / max) * 100, 3) + '%' });
    lane.appendChild(bar);
    wrap.appendChild(lane);
  });
  return wrap;
}
function renderFrame(f, stage) {
  stage.innerHTML = '';
  (f.rows || []).forEach((r) => stage.appendChild(renderRow(r)));
  if (f.gantt) stage.appendChild(renderGantt(f.gantt));
  if (f.svg) stage.appendChild(renderSvg(f.svg));
  if (f.table) stage.appendChild(renderTable(f.table));
  if (f.legend) {
    stage.appendChild(h('div', { class: 'legend' }, f.legend.map((l) => h('span', null, h('i', { style: 'background:' + l[0] }), l[1]))));
  }
}
const LEG_STD = [['var(--hl)', 'current'], ['var(--sel)', 'in range / pending'], ['var(--done)', 'done / found'], ['var(--pv)', 'pivot / special'], ['var(--bad)', 'rejected']];

/* ====================== the player (play / pause / step / speed) ====================== */
function mountPlayer(host, spec) {
  host.className = 'viz';
  host.innerHTML = '';
  const vals = {};
  (spec.inputs || []).forEach((i) => { vals[i.id] = i.value; });
  const state = { frames: [], idx: 0, timer: null, speed: 1 };
  const stage = h('div', { class: 'stage', 'aria-live': 'off' });
  const msg = h('div', { class: 'msg', role: 'status', 'aria-live': 'polite' });
  const pos = h('span', { class: 'pos' });
  const inputsBox = h('div', { class: 'inputs' });
  const refs = {};

  function stop() { if (state.timer) { clearTimeout(state.timer); state.timer = null; } btnPlay.textContent = '▶ Play'; }
  function show() {
    const f = state.frames[state.idx];
    if (!f) { stage.innerHTML = ''; return; }
    renderFrame(f, stage);
    msg.textContent = f.msg || '';
    pos.textContent = 'Step ' + (state.idx + 1) + ' / ' + state.frames.length;
    btnBack.disabled = state.idx === 0;
    btnNext.disabled = state.idx >= state.frames.length - 1;
  }
  function tick() {
    if (!host.isConnected) { stop(); return; }
    if (state.idx >= state.frames.length - 1) { stop(); return; }
    state.idx++; show();
    state.timer = setTimeout(tick, 900 / state.speed);
  }
  function run() {
    stop();
    try {
      (spec.inputs || []).forEach((i) => { vals[i.id] = refs[i.id].value; });
      state.frames = spec.build(Object.assign({}, vals));
      if (!state.frames.length) throw new Error('Nothing to show for this input.');
      state.idx = 0; show();
    } catch (e) {
      state.frames = [];
      stage.innerHTML = '';
      msg.textContent = 'Note: ' + e.message;
      pos.textContent = '';
      btnBack.disabled = btnNext.disabled = true;
    }
  }
  function refreshInputs() {
    (spec.inputs || []).forEach((i) => {
      const lab = refs['lab_' + i.id];
      if (i.label_fn) lab.firstChild.textContent = i.label_fn(readVals());
      if (i.show_fn) lab.style.display = i.show_fn(readVals()) ? '' : 'none';
    });
  }
  function readVals() { const v = {}; (spec.inputs || []).forEach((i) => { v[i.id] = refs[i.id].value; }); return v; }

  (spec.inputs || []).forEach((i) => {
    let el;
    if (i.type === 'select') {
      el = h('select', { id: undefined, 'aria-label': i.label }, i.options.map((o) => h('option', { value: o[0], text: o[1] })));
      el.value = i.value;
      el.addEventListener('change', () => {
        if (i.presets && i.presets[el.value]) { const p = i.presets[el.value]; for (const k in p) refs[k].value = p[k]; }
        refreshInputs(); run();
      });
    } else if (i.type === 'textarea') {
      el = h('textarea', { rows: i.rows || 5, 'aria-label': i.label }); el.value = i.value;
    } else {
      el = h('input', { type: i.type === 'number' ? 'number' : 'text', 'aria-label': i.label }); el.value = i.value;
      el.addEventListener('keydown', (e) => { if (e.key === 'Enter') run(); });
    }
    refs[i.id] = el;
    const lab = h('label', null, h('span', { text: i.label }), el);
    refs['lab_' + i.id] = lab;
    inputsBox.appendChild(lab);
  });
  const btnRun = h('button', { class: 'btn primary small', text: '↻ Apply input', onclick: run });
  if (spec.inputs && spec.inputs.length) inputsBox.appendChild(btnRun);

  const btnReset = h('button', { class: 'btn small', 'aria-label': 'Reset', text: '⏮ Reset', onclick: () => { stop(); state.idx = 0; show(); } });
  const btnBack = h('button', { class: 'btn small', 'aria-label': 'Step back', text: '◀ Back', onclick: () => { stop(); if (state.idx > 0) { state.idx--; show(); } } });
  const btnPlay = h('button', { class: 'btn primary small', 'aria-label': 'Play or pause', text: '▶ Play', onclick: () => {
    if (state.timer) { stop(); return; }
    if (state.idx >= state.frames.length - 1) { state.idx = 0; show(); }
    btnPlay.textContent = '⏸ Pause';
    state.timer = setTimeout(tick, 600 / state.speed);
  } });
  const btnNext = h('button', { class: 'btn small', 'aria-label': 'Step forward', text: 'Step ▶', onclick: () => { stop(); if (state.idx < state.frames.length - 1) { state.idx++; show(); } } });
  const speed = h('select', { 'aria-label': 'Animation speed' },
    [['0.5', '0.5x'], ['1', '1x'], ['2', '2x'], ['4', '4x']].map((o) => h('option', { value: o[0], text: 'Speed ' + o[1] })));
  speed.value = '1';
  speed.addEventListener('change', () => { state.speed = parseFloat(speed.value); });

  host.appendChild(h('header', null, h('b', { text: '' + spec.title }), spec.note ? h('span', { class: 'tip', text: spec.note }) : null));
  if (spec.inputs && spec.inputs.length) host.appendChild(inputsBox);
  host.appendChild(stage);
  host.appendChild(msg);
  host.appendChild(h('div', { class: 'controls' }, btnReset, btnBack, btnPlay, btnNext, speed, pos));
  refreshInputs();
  run();
}

/* ====================== visualiser registry ====================== */
const VIZ = {};
function sel(id, label, options, value, presets) { return { id: id, label: label, type: 'select', options: options, value: value, presets: presets }; }
function txt(id, label, value) { return { id: id, label: label, type: 'text', value: value }; }

/* ---------- complexity (live) ---------- */
VIZ.complexity = function () {
  return { live: function (host) {
    host.className = 'viz'; host.innerHTML = '';
    const curves = [
      ['O(1)', () => 1, '#0f9d6e'], ['O(log n)', (n) => Math.log2(Math.max(n, 1)), '#2563eb'], ['O(n)', (n) => n, '#e0a100'],
      ['O(n log n)', (n) => n * Math.log2(Math.max(n, 1)), '#f97316'], ['O(n²)', (n) => n * n, '#d6343f'], ['O(2ⁿ)', (n) => Math.pow(2, n), '#7c3aed'],
    ];
    const rng = h('input', { type: 'range', min: 5, max: 40, value: 16, 'aria-label': 'Maximum n for the graph' });
    const chartBox = h('div', { class: 'svgwrap' });
    const nInput = h('input', { type: 'number', value: 100000, min: 1, 'aria-label': 'Input size n' });
    const tbl = h('div', { class: 'tablewrap' });
    const note = h('div', { class: 'msg' });
    function draw() {
      const N = +rng.value, W = 640, H = 300, pad = 36, ymax = N * N * 0.6;
      const svg = s('svg', { viewBox: '0 0 ' + W + ' ' + H, width: W, height: H, role: 'img', 'aria-label': 'Growth of common complexities' });
      svg.appendChild(s('rect', { x: pad, y: 8, width: W - pad - 8, height: H - pad - 8, fill: 'none', stroke: 'var(--line)' }));
      curves.forEach((c, ci) => {
        let d = '';
        for (let n = 0; n <= N; n += N / 80) {
          const y = Math.min(c[1](n), ymax);
          const px = pad + (n / N) * (W - pad - 8), py = H - pad - (y / ymax) * (H - pad - 8);
          d += (d ? 'L' : 'M') + px.toFixed(1) + ' ' + py.toFixed(1);
        }
        svg.appendChild(s('path', { d: d, fill: 'none', stroke: c[2], 'stroke-width': 3, 'stroke-linecap': 'round' }));
        svg.appendChild(s('text', { x: W - 12, y: 24 + ci * 16, 'text-anchor': 'end', fill: c[2], 'font-size': 12, 'font-weight': 700 }, c[0]));
      });
      svg.appendChild(s('text', { x: W / 2, y: H - 8, 'text-anchor': 'middle', fill: 'var(--muted)', 'font-size': 12 }, 'input size n  (0 … ' + N + ')'));
      svg.appendChild(s('text', { x: 4, y: 20, fill: 'var(--muted)', 'font-size': 12 }, 'steps'));
      chartBox.innerHTML = ''; chartBox.appendChild(svg);
    }
    function fmt(x) { if (!isFinite(x) || x > 1e21) return 'astronomical'; if (x >= 1e6) return x.toExponential(2).replace('e+', ' × 10^'); return Math.round(x).toLocaleString(); }
    function table() {
      const n = Math.max(1, Math.floor(+nInput.value || 1));
      const rows = curves.map((c) => {
        const ops = c[0].indexOf('2') >= 0 && c[0].indexOf('n²') < 0 ? (n > 1000 ? Infinity : Math.pow(2, n)) : c[1](n);
        let verdict, cls;
        if (ops <= 1e8) { verdict = 'Fits in ~1 s ✔'; cls = 'Easy'; } else if (ops <= 1e9) { verdict = 'Borderline in Python ⚠'; cls = 'Medium'; } else { verdict = 'Too slow ✘'; cls = 'Hard'; }
        return h('tr', null, h('td', { class: 'mono', text: c[0] }), h('td', { class: 'mono', text: fmt(ops) }), h('td', null, h('span', { class: 'badge ' + cls, text: verdict })));
      });
      tbl.innerHTML = '';
      tbl.appendChild(h('table', null, h('tr', null, h('th', { text: 'Complexity' }), h('th', { text: 'Operations for n = ' + n.toLocaleString() }), h('th', { text: 'Typical 1-second budget (~10^7-10^8 simple steps)' })), rows));
      note.textContent = 'Try n = 20, 1,000, 100,000 and 1,000,000 to see which complexity classes survive.';
    }
    rng.addEventListener('input', draw); nInput.addEventListener('input', table);
    host.appendChild(h('header', null, h('b', { text: 'Growth curves and "will it pass?" estimator' })));
    host.appendChild(h('div', { class: 'inputs' }, h('label', null, h('span', { text: 'Graph range (max n)' }), rng), h('label', null, h('span', { text: 'Input size n for the estimator' }), nInput)));
    host.appendChild(h('div', { class: 'stage' }, chartBox, tbl));
    host.appendChild(note);
    draw(); table();
  } };
};

/* ---------- arrays ---------- */
VIZ.arr_ops = function (param) {
  const P = { reverse: '1,2,3,4,5,6', kadane: '-2,1,-3,4,-1,2,1,-5,4', prefix: '2,4,1,3,5', second: '3,1,4,4,2' };
  const presets = {}; Object.keys(P).forEach((k) => { presets[k] = { arr: P[k] }; });
  return { title: 'Array operations', inputs: [
    sel('algo', 'Algorithm', [['reverse', 'Reverse in place (two pointers)'], ['kadane', "Kadane's maximum subarray"], ['prefix', 'Prefix sums'], ['second', 'Second largest']], param || 'reverse', presets),
    txt('arr', 'Array (comma separated)', P[param || 'reverse']),
  ], build: function (v) {
    const a = parseNums(v.arr, { max: 12 }); const F = []; const n = a.length;
    if (v.algo === 'reverse') {
      const b = a.slice(); let lo = 0, hi = n - 1;
      F.push({ msg: 'Start: lo = 0 (left end), hi = ' + (n - 1) + ' (right end).', rows: [cellsRow('array', b, {}, { 0: 'lo', [n - 1]: 'hi' })] });
      while (lo < hi) {
        F.push({ msg: 'Swap a[' + lo + '] = ' + b[lo] + ' with a[' + hi + '] = ' + b[hi] + '.', rows: [cellsRow('array', b, { [lo]: 'hl', [hi]: 'hl' }, { [lo]: 'lo', [hi]: 'hi' })] });
        const t = b[lo]; b[lo] = b[hi]; b[hi] = t;
        F.push({ msg: 'Swapped. Move lo right and hi left.', rows: [cellsRow('array', b, { [lo]: 'sel', [hi]: 'sel' }, {})] });
        lo++; hi--;
      }
      F.push({ msg: 'lo ≥ hi: the array is reversed.  ' + n + ' elements, ' + Math.floor(n / 2) + ' swaps → O(n).', rows: [cellsRow('array', b, Object.fromEntries(b.map((_, i) => [i, 'ok'])), {})] });
    } else if (v.algo === 'kadane') {
      let cur = a[0], best = a[0], cs = 0, bs = 0, be = 0;
      const frame = (i, m) => {
        const marks = {};
        for (let k = bs; k <= be; k++) marks[k] = 'ok';
        for (let k = cs; k <= i; k++) marks[k] = marks[k] === 'ok' ? 'hl' : 'sel';
        F.push({ msg: m, rows: [cellsRow('array  (blue = current subarray, green = best so far)', a, marks, { [i]: 'x' }), kvRow('state', [{ k: 'cur', v: cur }, { k: 'best', v: best }])] });
      };
      frame(0, 'Start: cur = best = a[0] = ' + a[0] + '.');
      for (let i = 1; i < n; i++) {
        let m;
        if (a[i] > cur + a[i]) { m = 'a[' + i + '] = ' + a[i] + ' is better alone than cur + a[i] = ' + (cur + a[i]) + ' → restart here.'; cur = a[i]; cs = i; } else { m = 'Extend: cur = ' + cur + ' + ' + a[i] + ' = ' + (cur + a[i]) + '.'; cur += a[i]; }
        if (cur > best) { best = cur; bs = cs; be = i; m += ' New best = ' + best + '!'; }
        frame(i, m);
      }
      F.push({ msg: 'Answer: the maximum subarray sum is ' + best + ' (indices ' + bs + '..' + be + ').', rows: [cellsRow('array', a, Object.fromEntries(range(bs, be).map((k) => [k, 'ok'])), {})] });
    } else if (v.algo === 'prefix') {
      const P2 = [0];
      F.push({ msg: 'prefix[0] = 0 (the sum of nothing).', rows: [cellsRow('nums', a, {}, {}), cellsRow('prefix', P2, { 0: 'ok' }, {})] });
      for (let i = 0; i < n; i++) {
        P2.push(P2[i] + a[i]);
        F.push({ msg: 'prefix[' + (i + 1) + '] = prefix[' + i + '] + nums[' + i + '] = ' + P2[i] + ' + ' + a[i] + ' = ' + P2[i + 1], rows: [cellsRow('nums', a, { [i]: 'hl' }, {}), cellsRow('prefix', P2, { [i]: 'sel', [i + 1]: 'hl' }, {})] });
      }
      const l = Math.min(1, n - 1), r = Math.min(3, n - 1);
      F.push({ msg: 'Query sum of nums[' + l + '..' + r + '] = prefix[' + (r + 1) + '] − prefix[' + l + '] = ' + P2[r + 1] + ' − ' + P2[l] + ' = ' + (P2[r + 1] - P2[l]) + '.', rows: [cellsRow('nums', a, Object.fromEntries(range(l, r).map((k) => [k, 'ok'])), {}), cellsRow('prefix', P2, { [r + 1]: 'sel', [l]: 'pv' }, {})] });
    } else {
      let first = -Infinity, second = -Infinity;
      F.push({ msg: 'first = second = −∞.', rows: [cellsRow('array', a, {}, {}), kvRow('state', [{ k: 'first', v: '-inf' }, { k: 'second', v: '-inf' }])] });
      a.forEach((x, i) => {
        let m;
        if (x > first) { m = x + ' > first → old first becomes second, first = ' + x + '.'; second = first; first = x; } else if (x < first && x > second) { m = x + ' is between second and first → second = ' + x + '.'; second = x; } else m = x + ' changes nothing (duplicate or too small).';
        F.push({ msg: m, rows: [cellsRow('array', a, { [i]: 'hl' }, {}), kvRow('state', [{ k: 'first', v: first === -Infinity ? '-inf' : first }, { k: 'second', v: second === -Infinity ? '-inf' : second }])] });
      });
      F.push({ msg: second === -Infinity ? 'No second largest distinct value → return -1.' : 'Second largest = ' + second + '.', rows: [cellsRow('array', a, {}, {}), kvRow('answer', [{ k: 'second', v: second === -Infinity ? -1 : second, cls: 'hl' }])] });
    }
    return F;
  } };
};

VIZ.two_ptr = function () {
  return { title: 'Two pointers: pair sum in a sorted array', inputs: [txt('arr', 'Array (auto-sorted)', '1,3,4,6,8,11,15'), txt('t', 'Target sum', '14')],
    build: function (v) {
      const a = parseNums(v.arr, { sort: true, max: 14 }), t = +v.t, F = [];
      let lo = 0, hi = a.length - 1;
      F.push({ msg: 'Sorted array. lo at the smallest, hi at the largest. Looking for sum ' + t + '.', rows: [cellsRow('sorted array', a, {}, { [lo]: 'lo', [hi]: 'hi' })] });
      while (lo < hi) {
        const sum = a[lo] + a[hi];
        if (sum === t) { F.push({ msg: a[lo] + ' + ' + a[hi] + ' = ' + sum + ' = target ✔  Found the pair at indices ' + lo + ' and ' + hi + '.', rows: [cellsRow('sorted array', a, { [lo]: 'ok', [hi]: 'ok' }, { [lo]: 'lo', [hi]: 'hi' })] }); return F; }
        const dir = sum < t ? 'too small → move lo right (need a bigger value)' : 'too big → move hi left (need a smaller value)';
        F.push({ msg: a[lo] + ' + ' + a[hi] + ' = ' + sum + ' ' + (sum < t ? '<' : '>') + ' ' + t + ': ' + dir + '.', rows: [cellsRow('sorted array', a, { [lo]: 'hl', [hi]: 'hl' }, { [lo]: 'lo', [hi]: 'hi' })] });
        if (sum < t) lo++; else hi--;
      }
      F.push({ msg: 'Pointers crossed: no pair adds up to ' + t + '.', rows: [cellsRow('sorted array', a, Object.fromEntries(a.map((_, i) => [i, 'dim'])), {})] });
      return F;
    } };
};

VIZ.win_fixed = function () {
  return { title: 'Fixed-size sliding window', inputs: [txt('arr', 'Array', '2,1,5,1,3,2,8,1'), txt('k', 'Window size k', '3')],
    build: function (v) {
      const a = parseNums(v.arr, { max: 14 }), k = Math.floor(+v.k), F = [];
      if (!(k >= 1 && k <= a.length)) throw new Error('k must be between 1 and ' + a.length + '.');
      let w = 0; for (let i = 0; i < k; i++) w += a[i];
      let best = w, bi = 0;
      const win = (st, c) => Object.fromEntries(range(st, st + k - 1).map((i) => [i, c]));
      F.push({ msg: 'First window [0..' + (k - 1) + '] has sum ' + w + '.', rows: [cellsRow('array', a, win(0, 'sel'), {}), kvRow('state', [{ k: 'window sum', v: w }, { k: 'best', v: best }])] });
      for (let i = k; i < a.length; i++) {
        const out = a[i - k]; w += a[i] - out;
        const marks = win(i - k + 1, 'sel'); marks[i] = 'hl'; marks[i - k] = 'bad';
        if (w > best) { best = w; bi = i - k + 1; }
        F.push({ msg: 'Slide: add a[' + i + '] = ' + a[i] + ', drop a[' + (i - k) + '] = ' + out + ' → window sum ' + w + (w === best && bi === i - k + 1 ? '  (new best!)' : '') + '.', rows: [cellsRow('array (yellow enters, red leaves)', a, marks, {}), kvRow('state', [{ k: 'window sum', v: w }, { k: 'best', v: best }])] });
      }
      F.push({ msg: 'Done. Best window sum = ' + best + ' starting at index ' + bi + '.', rows: [cellsRow('array', a, win(bi, 'ok'), {}), kvRow('answer', [{ k: 'max sum', v: best, cls: 'hl' }])] });
      return F;
    } };
};

VIZ.win_var = function () {
  return { title: 'Variable window: longest substring without repeats', inputs: [txt('s', 'String', 'abcabcbb')],
    build: function (v) {
      const t = parseStr(v.s, 18), F = [], chars = t.split(''), last = {};
      let left = 0, best = 0, bl = 0;
      const lastKV = () => Object.keys(last).map((c) => ({ k: c, v: last[c] }));
      F.push({ msg: 'Window is empty. left = 0.', rows: [cellsRow('string', chars, {}, {}), kvRow('last index of each char', [])] });
      for (let r = 0; r < chars.length; r++) {
        const c = chars[r];
        if (c in last && last[c] >= left) {
          const mk2 = {}; range(left, r - 1).forEach((i) => { mk2[i] = 'sel'; }); mk2[last[c]] = 'bad'; mk2[r] = 'hl';
          F.push({ msg: "'" + c + "' already in the window at index " + last[c] + " → move left to " + (last[c] + 1) + '.', rows: [cellsRow('string', chars, mk2, { [left]: 'L', [r]: 'R' }), kvRow('last index of each char', lastKV())] });
          left = last[c] + 1;
        }
        last[c] = r;
        if (r - left + 1 > best) { best = r - left + 1; bl = left; }
        const mk3 = {}; range(left, r).forEach((i) => { mk3[i] = 'sel'; });
        F.push({ msg: "Add '" + c + "'. Window = \"" + t.slice(left, r + 1) + '" (length ' + (r - left + 1) + '). Best so far: ' + best + '.', rows: [cellsRow('string', chars, mk3, { [left]: 'L', [r]: 'R' }), kvRow('last index of each char', lastKV())] });
      }
      F.push({ msg: 'Longest substring without repeating characters: "' + t.slice(bl, bl + best) + '" (length ' + best + ').', rows: [cellsRow('string', chars, Object.fromEntries(range(bl, bl + best - 1).map((i) => [i, 'ok'])), {})] });
      return F;
    } };
};

/* ---------- strings ---------- */
VIZ.str_pal = function () {
  return { title: 'Palindrome check with two pointers', inputs: [txt('s', 'String', 'racecar')],
    build: function (v) {
      const t = parseStr(v.s, 18), c = t.split(''), F = [];
      let lo = 0, hi = c.length - 1; const done = {};
      F.push({ msg: 'Compare characters from both ends.', rows: [cellsRow('string', c, {}, { [lo]: 'lo', [hi]: 'hi' })] });
      while (lo < hi) {
        if (c[lo] === c[hi]) {
          done[lo] = 'ok'; done[hi] = 'ok';
          F.push({ msg: "'" + c[lo] + "' = '" + c[hi] + "' ✔ match. Move inward.", rows: [cellsRow('string', c, Object.assign({}, done), { [lo]: 'lo', [hi]: 'hi' })] });
          lo++; hi--;
        } else {
          F.push({ msg: "'" + c[lo] + "' ≠ '" + c[hi] + "' ✘ → not a palindrome.", rows: [cellsRow('string', c, Object.assign({}, done, { [lo]: 'bad', [hi]: 'bad' }), { [lo]: 'lo', [hi]: 'hi' })] });
          return F;
        }
      }
      F.push({ msg: 'Pointers met without a mismatch → palindrome ✔', rows: [cellsRow('string', c, Object.fromEntries(c.map((_, i) => [i, 'ok'])), {})] });
      return F;
    } };
};

VIZ.freq = function () {
  return { title: 'Character frequency map', inputs: [txt('s', 'Text', 'banana bread')],
    build: function (v) {
      const t = parseStr(v.s, 22), c = t.split(''), F = [], m = {};
      const kv = (cur) => Object.keys(m).map((k) => ({ k: k === ' ' ? '␣' : k, v: m[k], cls: k === cur ? 'hl' : '' }));
      F.push({ msg: 'Empty map. We will read the text one character at a time.', rows: [cellsRow('text', c, {}, {}), kvRow('counts', [])] });
      c.forEach((ch, i) => {
        m[ch] = (m[ch] || 0) + 1;
        const marks = {}; range(0, i - 1).forEach((k) => { marks[k] = 'ok'; }); marks[i] = 'hl';
        F.push({ msg: "Read '" + ch + "' → counts['" + ch + "'] = " + m[ch] + (m[ch] === 1 ? ' (new key)' : ''), rows: [cellsRow('text', c, marks, {}), kvRow('counts', kv(ch))] });
      });
      let bk = Object.keys(m)[0]; Object.keys(m).forEach((k) => { if (m[k] > m[bk]) bk = k; });
      const dups = Object.keys(m).filter((k) => m[k] > 1);
      F.push({ msg: "Most frequent: '" + bk + "' (" + m[bk] + '×). Characters appearing more than once: ' + (dups.join(' ') || 'none') + '.', rows: [cellsRow('text', c, Object.fromEntries(c.map((x, i) => [i, m[x] > 1 ? 'sel' : 'ok'])), {}), kvRow('counts', kv(bk))] });
      return F;
    } };
};

/* ---------- searching ---------- */
VIZ.bsearch = function (param) {
  return { title: 'Searching', inputs: [
    sel('mode', 'Algorithm', [['classic', 'Binary search'], ['first', 'First occurrence'], ['last', 'Last occurrence'], ['linear', 'Linear search (compare)']], param || 'classic', { classic: { t: '12' }, first: { t: '7' }, last: { t: '7' }, linear: { t: '12' } }),
    txt('arr', 'Array (auto-sorted)', '1,3,3,5,7,7,7,9,12,15'), txt('t', 'Target', (param === 'first' || param === 'last') ? '7' : '12')],
    build: function (v) {
      const a = parseNums(v.arr, { sort: true, max: 16 }), t = +v.t, F = [], n = a.length;
      if (v.mode === 'linear') {
        for (let i = 0; i < n; i++) {
          const marks = {}; range(0, i - 1).forEach((k) => { marks[k] = 'dim'; });
          if (a[i] === t) { marks[i] = 'ok'; F.push({ msg: 'a[' + i + '] = ' + a[i] + ' = target ✔ found after ' + (i + 1) + ' comparison(s).', rows: [cellsRow('array', a, marks, { [i]: 'i' })] }); return F; }
          marks[i] = 'hl';
          F.push({ msg: 'a[' + i + '] = ' + a[i] + ' ≠ ' + t + '. Check the next element.', rows: [cellsRow('array', a, marks, { [i]: 'i' })] });
        }
        F.push({ msg: 'Reached the end: ' + t + ' is not in the array (' + n + ' comparisons).', rows: [cellsRow('array', a, {}, {})] });
        return F;
      }
      let lo = 0, hi = n - 1, ans = -1, steps = 0;
      const view = (mid, hl) => {
        const marks = {}; a.forEach((_, i) => { if (i < lo || i > hi) marks[i] = 'dim'; });
        if (mid !== null) marks[mid] = hl || 'hl';
        if (ans >= 0) marks[ans] = 'ok';
        const tags = {}; if (lo <= hi) { tags[lo] = 'lo'; tags[hi] = (tags[hi] ? tags[hi] + ',' : '') + 'hi'; } if (mid !== null) tags[mid] = (tags[mid] ? tags[mid] + ',' : '') + 'mid';
        return cellsRow('array  (grey = discarded)', a, marks, tags);
      };
      F.push({ msg: 'Search window is the whole array: lo = 0, hi = ' + (n - 1) + '. Target = ' + t + '.', rows: [view(null)] });
      while (lo <= hi) {
        const mid = (lo + hi) >> 1; steps++;
        if (a[mid] === t) {
          if (v.mode === 'classic') { F.push({ msg: 'mid = ' + mid + ', a[mid] = ' + a[mid] + ' = target ✔ found after ' + steps + ' step(s).', rows: [view(mid, 'ok')] }); return F; }
          ans = mid;
          F.push({ msg: 'a[' + mid + '] = ' + t + ' matches. Remember ans = ' + mid + ' and keep searching ' + (v.mode === 'first' ? 'LEFT' : 'RIGHT') + ' for another match.', rows: [view(mid, 'ok')] });
          if (v.mode === 'first') hi = mid - 1; else lo = mid + 1;
        } else if (a[mid] < t) {
          F.push({ msg: 'mid = ' + mid + ': a[mid] = ' + a[mid] + ' < ' + t + ' → discard the left half, lo = ' + (mid + 1) + '.', rows: [view(mid)] });
          lo = mid + 1;
        } else {
          F.push({ msg: 'mid = ' + mid + ': a[mid] = ' + a[mid] + ' > ' + t + ' → discard the right half, hi = ' + (mid - 1) + '.', rows: [view(mid)] });
          hi = mid - 1;
        }
      }
      F.push({ msg: ans >= 0 ? 'Window is empty. ' + (v.mode === 'first' ? 'First' : 'Last') + ' occurrence of ' + t + ' is at index ' + ans + '.' : 'Window is empty: ' + t + ' is not in the array → return -1 (after ' + steps + ' steps).', rows: [view(null)] });
      return F;
    } };
};

VIZ.bs_answer = function () {
  return { title: 'Binary search on the answer (eating bananas)', note: 'Find the slowest speed that finishes in h hours', inputs: [txt('piles', 'Piles', '3,6,7,11'), txt('hh', 'Hours h', '8')],
    build: function (v) {
      const p = parseNums(v.piles, { max: 10, int: true, min: 1 }), H = Math.floor(+v.hh), F = [];
      if (!(H >= p.length)) throw new Error('h must be at least the number of piles (' + p.length + ').');
      let lo = 1, hi = Math.max(...p);
      const rangeRow = () => cellsRow('candidate speeds still possible: lo..hi', range(lo, hi), {}, {}, true);
      F.push({ msg: 'The answer is a speed between ' + lo + ' and ' + hi + '. We binary search that range, not the piles.', rows: [cellsRow('piles', p, {}, {}), rangeRow()] });
      while (lo < hi) {
        const mid = (lo + hi) >> 1; const hrs = p.map((x) => Math.ceil(x / mid)); const tot = hrs.reduce((a, b) => a + b, 0);
        const ok = tot <= H;
        F.push({ msg: 'Try speed ' + mid + ': hours per pile = [' + hrs.join(', ') + '] → total ' + tot + (ok ? ' ≤ ' : ' > ') + H + (ok ? '  ✔ feasible → try slower: hi = ' + mid : '  ✘ too slow → lo = ' + (mid + 1)) + '.', rows: [cellsRow('piles (tag = hours at this speed)', p, Object.fromEntries(p.map((_, i) => [i, ok ? 'ok' : 'bad'])), Object.fromEntries(hrs.map((x, i) => [i, x + 'h']))), cellsRow('speeds (lo..hi)', range(lo, hi), { [mid - lo]: ok ? 'ok' : 'bad' }, { [mid - lo]: 'mid' }, true)] });
        if (ok) hi = mid; else lo = mid + 1;
      }
      F.push({ msg: 'lo = hi = ' + lo + ' → the minimum speed is ' + lo + '.', rows: [cellsRow('piles', p, {}, {}), cellsRow('answer', [lo], { 0: 'ok' }, {}, true)] });
      return F;
    } };
};

/* ---------- sorting ---------- */
VIZ.sort = function (param) {
  return { title: 'Sorting algorithms', inputs: [
    sel('algo', 'Algorithm', [['bubble', 'Bubble sort'], ['selection', 'Selection sort'], ['insertion', 'Insertion sort'], ['merge', 'Merge sort'], ['quick', 'Quick sort (Lomuto)'], ['heap', 'Heap sort'], ['counting', 'Counting sort']], param || 'bubble'),
    txt('arr', 'Array (up to 12 values)', '6,3,8,2,9,1,5')],
    build: function (v) {
      const orig = parseNums(v.arr, { max: 12, int: true, min: 0 }); const a = orig.slice(), n = a.length, F = [];
      let cmp = 0, mv = 0;
      const stats = () => ' [comparisons: ' + cmp + ', swaps/writes: ' + mv + ']';
      const snap = (m, marks) => F.push({ msg: m + stats(), rows: [barsRow(a, marks || {})], legend: LEG_STD });
      const sorted = Object.fromEntries(a.map((_, i) => [i, 'ok']));
      const swap = (i, j) => { const t = a[i]; a[i] = a[j]; a[j] = t; mv++; };
      snap('Start: unsorted array.');
      const al = v.algo;
      if (al === 'bubble') {
        const done = {};
        for (let i = 0; i < n - 1; i++) {
          let sw = false;
          for (let j = 0; j < n - 1 - i; j++) {
            cmp++; snap('Compare ' + a[j] + ' and ' + a[j + 1] + '.', Object.assign({}, done, { [j]: 'hl', [j + 1]: 'hl' }));
            if (a[j] > a[j + 1]) { swap(j, j + 1); sw = true; snap('Out of order → swap.', Object.assign({}, done, { [j]: 'sel', [j + 1]: 'sel' })); }
          }
          done[n - 1 - i] = 'ok';
          snap('End of pass ' + (i + 1) + ': the largest remaining value bubbled to the end.', Object.assign({}, done));
          if (!sw) break;
        }
      } else if (al === 'selection') {
        const done = {};
        for (let i = 0; i < n - 1; i++) {
          let m = i;
          for (let j = i + 1; j < n; j++) { cmp++; snap('Looking for the minimum: current min ' + a[m] + ', checking ' + a[j] + '.', Object.assign({}, done, { [m]: 'pv', [j]: 'hl' })); if (a[j] < a[m]) m = j; }
          if (m !== i) swap(i, m);
          done[i] = 'ok'; snap('Place the minimum ' + a[i] + ' at position ' + i + '.', Object.assign({}, done));
        }
      } else if (al === 'insertion') {
        for (let i = 1; i < n; i++) {
          const key = a[i]; let j = i - 1;
          snap('Take key = ' + key + ' and insert it into the sorted left part.', { [i]: 'pv' });
          while (j >= 0) {
            cmp++;
            if (a[j] > key) { a[j + 1] = a[j]; mv++; snap(a[j] + ' > ' + key + ' → shift right.', { [j]: 'hl', [j + 1]: 'sel' }); j--; } else break;
          }
          a[j + 1] = key; mv++;
          const mk3 = {}; range(0, i).forEach((x) => { mk3[x] = 'ok'; }); mk3[j + 1] = 'pv';
          snap('Drop key into position ' + (j + 1) + '.', mk3);
        }
      } else if (al === 'merge') {
        const ms = (lo, hi) => {
          if (lo >= hi) return;
          const mid = (lo + hi) >> 1; ms(lo, mid); ms(mid + 1, hi);
          const L = a.slice(lo, mid + 1), R = a.slice(mid + 1, hi + 1); let i = 0, j = 0, k = lo;
          const rng = {}; range(lo, hi).forEach((x) => { rng[x] = 'sel'; });
          snap('Merge sorted halves [' + L.join(',') + '] and [' + R.join(',') + '].', rng);
          while (i < L.length || j < R.length) {
            if (j >= R.length || (i < L.length && L[i] <= R[j])) { cmp += j < R.length ? 1 : 0; a[k] = L[i++]; } else { cmp++; a[k] = R[j++]; }
            mv++; snap('Write ' + a[k] + ' to position ' + k + '.', Object.assign({}, rng, { [k]: 'ok' })); k++;
          }
        };
        ms(0, n - 1);
      } else if (al === 'quick') {
        const fixed = {};
        const qs = (lo, hi) => {
          if (lo > hi) return;
          if (lo === hi) { fixed[lo] = 'ok'; snap('Single element ' + a[lo] + ' is in place.', Object.assign({}, fixed)); return; }
          const p = a[hi]; let i = lo - 1;
          snap('Partition [' + lo + '..' + hi + '] with pivot = ' + p + ' (last element).', Object.assign({}, fixed, { [hi]: 'pv' }));
          for (let j = lo; j < hi; j++) {
            cmp++;
            if (a[j] <= p) { i++; if (i !== j) swap(i, j); snap(a[i] + ' ≤ ' + p + ' → goes to the left side.', Object.assign({}, fixed, { [hi]: 'pv', [i]: 'sel', [j]: 'hl' })); } else snap(a[j] + ' > ' + p + ' → stays on the right side.', Object.assign({}, fixed, { [hi]: 'pv', [j]: 'hl' }));
          }
          swap(i + 1, hi); fixed[i + 1] = 'ok';
          snap('Put the pivot ' + p + ' in its final position ' + (i + 1) + '.', Object.assign({}, fixed));
          qs(lo, i); qs(i + 2, hi);
        };
        qs(0, n - 1);
      } else if (al === 'heap') {
        const sd = (i, size) => {
          for (;;) {
            let big = i; const l = 2 * i + 1, r = 2 * i + 2;
            if (l < size) { cmp++; if (a[l] > a[big]) big = l; }
            if (r < size) { cmp++; if (a[r] > a[big]) big = r; }
            if (big === i) return;
            snap('Sift down: swap ' + a[i] + ' with larger child ' + a[big] + '.', { [i]: 'hl', [big]: 'sel' });
            swap(i, big); i = big;
          }
        };
        snap('Phase 1: build a max-heap (parent ≥ children) from the array.');
        for (let i = (n >> 1) - 1; i >= 0; i--) sd(i, n);
        snap('Max-heap built: the largest value is at index 0.', { 0: 'pv' });
        const done = {};
        for (let end = n - 1; end > 0; end--) {
          snap('Phase 2: swap the max ' + a[0] + ' with the last heap element.', Object.assign({}, done, { 0: 'hl', [end]: 'hl' }));
          swap(0, end); done[end] = 'ok'; sd(0, end);
          snap('Heap shrinks; ' + a[end] + ' is in its final place.', Object.assign({}, done));
        }
      } else if (al === 'counting') {
        const mx = Math.max(...a); const counts = new Array(mx + 1).fill(0);
        a.forEach((x, i) => { counts[x]++; F.push({ msg: 'Count ' + x + ': counts[' + x + '] = ' + counts[x] + '.', rows: [barsRow(a, { [i]: 'hl' }), cellsRow('counts (index = value)', counts, { [x]: 'hl' }, {})], legend: LEG_STD }); });
        const out = []; let w = 0;
        counts.forEach((c, val) => { for (let k = 0; k < c; k++) { out.push(val); w++; F.push({ msg: 'Output ' + val + ' (' + c + ' copies in total).', rows: [barsRow(out.concat(Array(n - out.length).fill(0)), Object.fromEntries(range(0, out.length - 1).map((i) => [i, i === out.length - 1 ? 'hl' : 'ok']))), cellsRow('counts', counts, { [val]: 'hl' }, {})], legend: LEG_STD }); } });
        for (let i = 0; i < n; i++) a[i] = out[i]; mv = w;
      }
      F.push({ msg: 'Sorted ✔' + stats() + '   Expected complexity: ' + ({ bubble: 'O(n²), O(n) best', selection: 'O(n²) always', insertion: 'O(n²), O(n) best', merge: 'O(n log n) always, O(n) extra space', quick: 'O(n log n) average, O(n²) worst', heap: 'O(n log n) always, O(1) space', counting: 'O(n + k)' })[al], rows: [barsRow(a, sorted)], legend: LEG_STD });
      return F;
    } };
};

/* ---------- hashing ---------- */
VIZ.hash = function () {
  return { title: 'Hash table with chaining', inputs: [txt('keys', 'Keys to insert (comma separated)', 'cat,dog,act,tac,bird,21,14'), txt('size', 'Table size', '7'), txt('q', 'Look up key', 'tac')],
    build: function (v) {
      const keys = String(v.keys).split(/[\s,]+/).filter(Boolean); const size = Math.floor(+v.size);
      if (!keys.length || keys.length > 12) throw new Error('Enter 1 to 12 keys.');
      if (!(size >= 2 && size <= 11)) throw new Error('Table size must be between 2 and 11.');
      const hf = (k) => /^-?\d+$/.test(k) ? Math.abs(parseInt(k, 10)) % size : k.split('').reduce((a, c) => a + c.charCodeAt(0), 0) % size;
      const hexp = (k) => /^-?\d+$/.test(k) ? k + ' % ' + size : '(' + k.split('').map((c) => c.charCodeAt(0)).join('+') + ') % ' + size;
      const B = range(0, size - 1).map(() => []); const F = [];
      const rows = (hl, cls) => B.map((b, i) => cellsRow('bucket ' + i, b, Object.fromEntries(b.map((_, j) => [j, i === hl ? (cls || 'hl') : ''])), {}, true));
      F.push({ msg: 'Empty table with ' + size + ' buckets. hash(key) = sum of character codes (or the number itself) mod ' + size + '.', rows: rows(-1) });
      keys.forEach((k) => {
        const i = hf(k); const coll = B[i].length > 0;
        B[i].push(k);
        F.push({ msg: 'hash("' + k + '") = ' + hexp(k) + ' = ' + i + (coll ? ' → bucket ' + i + ' is occupied: COLLISION, chain the key.' : ' → empty bucket, store it.'), rows: rows(i, coll ? 'bad' : 'ok') });
      });
      const q = String(v.q).trim();
      if (q) {
        const i = hf(q); const pos = B[i].indexOf(q);
        F.push({ msg: 'Lookup "' + q + '": hash = ' + i + '. Jump straight to bucket ' + i + ' (no scan of other buckets).', rows: rows(i, 'sel') });
        F.push({ msg: pos >= 0 ? 'Found "' + q + '" at position ' + pos + ' of the chain ✔ (average O(1); longest chain here = ' + Math.max(...B.map((b) => b.length)) + ').' : '"' + q + '" is not in bucket ' + i + ' → not present.', rows: B.map((b, bi) => cellsRow('bucket ' + bi, b, Object.fromEntries(b.map((x, j) => [j, bi === i && j === pos ? 'ok' : ''])), {}, true)) });
      }
      return F;
    } };
};

VIZ.twosum = function () {
  return { title: 'Two Sum with a hash map', inputs: [txt('arr', 'Array', '2,7,11,15,3'), txt('t', 'Target', '9')],
    build: function (v) {
      const a = parseNums(v.arr, { max: 12 }), t = +v.t, F = [], seen = {};
      const kv = (hl) => Object.keys(seen).map((k) => ({ k: k, v: 'idx ' + seen[k], cls: String(hl) === k ? 'hl' : '' }));
      F.push({ msg: 'Scan left to right. For each x we look for the partner target − x = ' + t + ' − x in the map.', rows: [cellsRow('array', a, {}, {}), kvRow('seen: value → index', [])] });
      for (let i = 0; i < a.length; i++) {
        const need = t - a[i];
        if (String(need) in seen) {
          F.push({ msg: 'x = ' + a[i] + ', need = ' + need + ' is in the map (index ' + seen[need] + ') ✔ → answer [' + seen[need] + ', ' + i + '].', rows: [cellsRow('array', a, { [i]: 'ok', [seen[need]]: 'ok' }, {}), kvRow('seen: value → index', kv(need))] });
          return F;
        }
        F.push({ msg: 'x = ' + a[i] + ', need = ' + need + ' not seen yet → store ' + a[i] + ' → ' + i + '.', rows: [cellsRow('array', a, { [i]: 'hl' }, {}), kvRow('seen: value → index', kv())] });
        seen[a[i]] = i;
      }
      F.push({ msg: 'No pair adds up to ' + t + '.', rows: [cellsRow('array', a, {}, {}), kvRow('seen', kv())] });
      return F;
    } };
};

/* ---------- stacks & queues ---------- */
VIZ.stack = function () {
  return { live: function (host) {
    host.className = 'viz'; host.innerHTML = '';
    const st = [];
    const stage = h('div', { class: 'stage' }), msg = h('div', { class: 'msg', text: 'Push some values. The LAST value pushed is the FIRST one popped (LIFO).' });
    const inp = h('input', { type: 'text', value: '7', 'aria-label': 'Value to push', style: 'width:90px' });
    function draw(m, hl) {
      if (m) msg.textContent = m;
      stage.innerHTML = '';
      stage.appendChild(renderRow({ kind: 'stack', label: 'stack (top is the highest box)', items: st.map((x, i) => ({ v: x, cls: i === st.length - 1 ? (hl || 'hl') : '' })) }));
      stage.appendChild(h('div', { class: 'tip', text: 'size = ' + st.length + ',  peek() = ' + (st.length ? st[st.length - 1] : 'None (empty)') }));
    }
    const push = () => { if (st.length >= 12) { draw('Stack is capped at 12 items in this demo.'); return; } st.push(inp.value.trim() || '0'); draw('push(' + st[st.length - 1] + ') → it lands on top. O(1).', 'ok'); };
    const pop = () => { if (!st.length) { draw('Note: pop from an empty stack → IndexError in Python. Always check first!', 'bad'); return; } const x = st.pop(); draw('pop() returned ' + x + ' - the most recent item. O(1).'); };
    const peek = () => draw(st.length ? 'peek() = ' + st[st.length - 1] + ' (stack unchanged).' : 'Stack empty: nothing to peek.');
    host.appendChild(h('header', null, h('b', { text: 'Stack (LIFO) - try it' })));
    host.appendChild(h('div', { class: 'inputs' }, h('label', null, h('span', { text: 'Value' }), inp), h('button', { class: 'btn primary small', text: 'push', onclick: push }), h('button', { class: 'btn small', text: 'pop', onclick: pop }), h('button', { class: 'btn small', text: 'peek', onclick: peek }), h('button', { class: 'btn small', text: 'clear', onclick: () => { st.length = 0; draw('Cleared.'); } })));
    host.appendChild(stage); host.appendChild(msg); draw();
  } };
};

VIZ.queue = function () {
  return { live: function (host) {
    host.className = 'viz'; host.innerHTML = '';
    let q = []; let kind = 'queue';
    const stage = h('div', { class: 'stage' }), msg = h('div', { class: 'msg', text: 'Enqueue values at the back; dequeue from the front (FIFO).' });
    const inp = h('input', { type: 'text', value: '5', 'aria-label': 'Value', style: 'width:90px' });
    const typ = h('select', { 'aria-label': 'Structure type' }, [['queue', 'Queue (FIFO)'], ['deque', 'Deque (both ends)'], ['pq', 'Priority queue (min-heap order)']].map((o) => h('option', { value: o[0], text: o[1] })));
    const bar = h('div', { class: 'inputs' });
    function buttons() {
      bar.innerHTML = '';
      bar.appendChild(h('label', null, h('span', { text: 'Type' }), typ));
      bar.appendChild(h('label', null, h('span', { text: 'Value' }), inp));
      if (kind === 'queue') { bar.appendChild(h('button', { class: 'btn primary small', text: 'enqueue (back)', onclick: () => add('back') })); bar.appendChild(h('button', { class: 'btn small', text: 'dequeue (front)', onclick: () => rem('front') })); }
      if (kind === 'deque') { bar.appendChild(h('button', { class: 'btn primary small', text: 'append (back)', onclick: () => add('back') })); bar.appendChild(h('button', { class: 'btn primary small', text: 'appendleft (front)', onclick: () => add('front') })); bar.appendChild(h('button', { class: 'btn small', text: 'popleft', onclick: () => rem('front') })); bar.appendChild(h('button', { class: 'btn small', text: 'pop', onclick: () => rem('back') })); }
      if (kind === 'pq') { bar.appendChild(h('button', { class: 'btn primary small', text: 'heappush', onclick: () => add('pq') })); bar.appendChild(h('button', { class: 'btn small', text: 'heappop (smallest)', onclick: () => rem('pq') })); }
    }
    function draw(m, hlIdx, cls) {
      if (m) msg.textContent = m;
      stage.innerHTML = '';
      const tags = {}; if (q.length) { tags[0] = kind === 'pq' ? 'min' : 'front'; tags[q.length - 1] = (tags[q.length - 1] ? tags[q.length - 1] + '/' : '') + (kind === 'pq' ? '' : 'back'); }
      stage.appendChild(renderRow(cellsRow(kind === 'pq' ? 'items (shown in sorted order; a real heap only guarantees the smallest is first)' : 'items', q, hlIdx !== undefined ? { [hlIdx]: cls || 'hl' } : {}, tags)));
      stage.appendChild(h('div', { class: 'tip', text: 'size = ' + q.length }));
    }
    function add(where) {
      if (q.length >= 12) { draw('Capped at 12 items in this demo.'); return; }
      const val = inp.value.trim() || '0';
      if (where === 'back') { q.push(val); draw(kind === 'queue' ? 'enqueue(' + val + ') → joins the back of the line. O(1) with collections.deque.' : 'append(' + val + ') at the back. O(1).', q.length - 1, 'ok'); }
      else if (where === 'front') { q.unshift(val); draw('appendleft(' + val + ') at the front. O(1) for a deque (list.insert(0) would be O(n)).', 0, 'ok'); }
      else { q.push(val); q.sort((a, b) => (isNaN(a) || isNaN(b) ? String(a).localeCompare(String(b)) : a - b)); draw('heappush(' + val + ') - O(log n). The smallest value is always at the front.', q.indexOf(val), 'ok'); }
    }
    function rem(where) {
      if (!q.length) { draw('Note: Nothing to remove - the structure is empty.'); return; }
      const x = where === 'back' ? q.pop() : q.shift();
      draw((where === 'back' ? 'pop()' : kind === 'queue' ? 'dequeue()' : kind === 'pq' ? 'heappop()' : 'popleft()') + ' returned ' + x + '.');
    }
    typ.addEventListener('change', () => { kind = typ.value; q = []; buttons(); draw('Switched to ' + typ.options[typ.selectedIndex].text + '.'); });
    host.appendChild(h('header', null, h('b', { text: 'Queue, deque and priority queue - try it' })));
    host.appendChild(bar); host.appendChild(stage); host.appendChild(msg); buttons(); draw();
  } };
};

VIZ.paren = function () {
  return { title: 'Balanced brackets with a stack', inputs: [txt('s', 'Brackets', '{[()]}[')],
    build: function (v) {
      const t = String(v.s).replace(/\s/g, ''); if (!t || t.length > 16 || /[^()\[\]{}]/.test(t)) throw new Error('Use up to 16 characters from ()[]{} only.');
      const c = t.split(''), F = [], st = [], pairs = { ')': '(', ']': '[', '}': '{' };
      const view = (i, cls) => [cellsRow('input', c, Object.fromEntries(c.map((_, k) => [k, k < i ? 'ok' : k === i ? (cls || 'hl') : ''])), {}), stackRow('stack', st)];
      F.push({ msg: 'Scan left to right. Push openers; closers must match the top of the stack.', rows: view(-1) });
      for (let i = 0; i < c.length; i++) {
        const ch = c[i];
        if ('([{'.includes(ch)) { st.push(ch); F.push({ msg: "'" + ch + "' is an opener → push.", rows: view(i) }); } else if (!st.length) { F.push({ msg: "'" + ch + "' is a closer but the stack is empty ✘ → not balanced.", rows: view(i, 'bad') }); return F; } else if (st[st.length - 1] !== pairs[ch]) { F.push({ msg: "'" + ch + "' needs '" + pairs[ch] + "' but the top is '" + st[st.length - 1] + "' ✘ → not balanced.", rows: view(i, 'bad') }); return F; } else { st.pop(); F.push({ msg: "'" + ch + "' matches the top → pop.", rows: view(i) }); }
      }
      F.push({ msg: st.length ? 'Input finished but ' + st.length + ' opener(s) are still on the stack ✘ → not balanced.' : 'Input finished and the stack is empty ✔ → balanced.', rows: view(c.length) });
      return F;
    } };
};

VIZ.nge = function () {
  return { title: 'Monotonic stack: next greater element', inputs: [txt('arr', 'Array', '4,5,2,25,7,8')],
    build: function (v) {
      const a = parseNums(v.arr, { max: 12 }), n = a.length, res = new Array(n).fill(-1), st = [], F = [];
      const view = (i, m, extra) => F.push({ msg: m, rows: [cellsRow('array', a, Object.assign({ [i]: 'hl' }, extra || {}), {}), cellsRow('answers (−1 = none yet)', res, Object.fromEntries(res.map((r, k) => [k, r !== -1 ? 'ok' : ''])), {}), stackRow('stack of indices waiting: ' + st.map((k) => 'i' + k + '=' + a[k]).join(', '), st.map((k) => 'i' + k))] });
      view(-1, 'Stack holds indices whose "next greater" is still unknown.');
      for (let i = 0; i < n; i++) {
        while (st.length && a[st[st.length - 1]] < a[i]) { const j = st.pop(); res[j] = a[i]; view(i, a[i] + ' > a[' + j + '] = ' + a[j] + ' → next greater of index ' + j + ' is ' + a[i] + '. Pop it.', { [j]: 'ok' }); }
        st.push(i); view(i, 'Push index ' + i + ' (value ' + a[i] + ').');
      }
      view(-1, 'Remaining stack entries have no greater element → stay −1. Each index was pushed and popped once → O(n).');
      return F;
    } };
};

/* ---------- linked lists ---------- */
function llRow(label, vals, marks, tags, opts) {
  return cellsRow(label, vals, marks, tags, true);
}
VIZ.ll = function () {
  return { live: function (host) {
    host.className = 'viz'; host.innerHTML = '';
    let L = [3, 7, 1]; let kind = 'single';
    const stage = h('div', { class: 'stage' }), msg = h('div', { class: 'msg', text: 'Each node stores a value and a pointer to the next node.' });
    const inp = h('input', { type: 'text', value: '9', 'aria-label': 'Value', style: 'width:80px' });
    const typ = h('select', { 'aria-label': 'List type' }, [['single', 'Singly linked'], ['double', 'Doubly linked'], ['circular', 'Circular']].map((o) => h('option', { value: o[0], text: o[1] })));
    function draw(m, hl, cls) {
      if (m) msg.textContent = m;
      stage.innerHTML = '';
      const arrow = kind === 'double' ? ' ⇄ ' : ' → ';
      const wrap = h('div', { class: 'cells', style: 'align-items:center' });
      wrap.appendChild(h('div', { class: 'tag', text: 'head' }));
      wrap.appendChild(h('span', { text: '▶' }));
      L.forEach((x, i) => {
        wrap.appendChild(h('div', { class: 'cell ' + (i === hl ? cls || 'hl' : ''), text: String(x), style: 'border-radius:9px;min-width:54px' }));
        wrap.appendChild(h('span', { class: 'mono', text: i < L.length - 1 ? arrow : '' }));
      });
      wrap.appendChild(h('span', { class: 'mono', text: L.length ? (kind === 'circular' ? '  ↺ back to head' : ' → None') : 'head = None (empty list)' }));
      stage.appendChild(wrap);
      stage.appendChild(h('div', { class: 'tip', style: 'margin-top:8px', text: kind === 'double' ? 'Each node also keeps a prev pointer, so deleting a known node is O(1) and you can walk backwards.' : kind === 'circular' ? 'The last node points back to the head, so traversal needs a stopping rule (stop when you return to head).' : 'Length ' + L.length + '. Access by index needs a walk from head: O(n).' }));
    }
    const v = () => inp.value.trim() || '0';
    const ops = [
      ['insert at head', () => { L.unshift(v()); draw('Insert at head: new.next = head; head = new → O(1).', 0, 'ok'); }],
      ['insert at tail', () => { L.push(v()); draw('Insert at tail: walk to the last node (O(n), or O(1) with a tail pointer).', L.length - 1, 'ok'); }],
      ['delete value', () => { const i = L.indexOf(v()); if (i < 0) { draw('Value ' + v() + ' not found - nothing deleted.'); return; } L.splice(i, 1); draw('Deleted the first node with value ' + v() + ': previous.next = node.next.'); }],
      ['search', () => { const i = L.indexOf(v()); draw(i >= 0 ? 'Found ' + v() + ' at position ' + i + ' after visiting ' + (i + 1) + ' node(s) - O(n).' : v() + ' is not in the list (visited all ' + L.length + ' nodes).', i >= 0 ? i : undefined, 'ok'); }],
      ['reverse', () => { L.reverse(); draw('Reversed by flipping every next pointer (see the Reversal animation for the pointer-by-pointer view).'); }],
      ['reset', () => { L = ['3', '7', '1']; draw('Reset.'); }],
    ];
    L = L.map(String);
    typ.addEventListener('change', () => { kind = typ.value; draw(); });
    host.appendChild(h('header', null, h('b', { text: 'Linked list - try it' })));
    host.appendChild(h('div', { class: 'inputs' }, h('label', null, h('span', { text: 'List type' }), typ), h('label', null, h('span', { text: 'Value' }), inp), ops.map((o) => h('button', { class: 'btn small', text: o[0], onclick: o[1] }))));
    host.appendChild(stage); host.appendChild(msg); draw();
  } };
};

VIZ.ll_reverse = function () {
  return { title: 'Reversing a linked list (prev / cur / nxt)', inputs: [txt('arr', 'List values', '1,2,3,4,5')],
    build: function (v) {
      const a = parseNums(v.arr, { max: 8 }), n = a.length, F = [];
      const nxt = a.map((_, i) => (i + 1 < n ? i + 1 : -1));
      let prev = -1, cur = 0;
      const chain = (start, label, cls) => { const out = [], mk3 = {}; let p = start, g = 0; while (p !== -1 && g++ < 20) { mk3[out.length] = cls; out.push(a[p]); p = nxt[p]; } return cellsRow(label, out, mk3, {}, true); };
      const view = (m, hlCur) => F.push({ msg: m, rows: [chain(prev, 'reversed part  (prev → …)', 'ok'), chain(cur, 'remaining part  (cur → …)', hlCur ? 'hl' : 'sel'), kvRow('pointers', [{ k: 'prev', v: prev === -1 ? 'None' : a[prev] }, { k: 'cur', v: cur === -1 ? 'None' : a[cur], cls: 'hl' }])] });
      view('Start: prev = None, cur = head.');
      while (cur !== -1) {
        const nx = nxt[cur];
        view('1) nxt = cur.next (remember the rest: ' + (nx === -1 ? 'None' : a[nx]) + ').', true);
        nxt[cur] = prev; view('2) cur.next = prev → the arrow of node ' + a[cur] + ' now points backwards.', true);
        prev = cur; cur = nx; view('3) prev = cur; cur = nxt → advance both pointers.');
      }
      view('cur is None → return prev. The new head is ' + a[prev] + '. O(n) time, O(1) space.');
      return F;
    } };
};

VIZ.ll_cycle = function () {
  return { title: "Floyd's slow / fast pointers", inputs: [txt('arr', 'List values', '3,2,0,-4,6,8'), txt('pos', 'Tail connects back to index (−1 = no cycle)', '2')],
    build: function (v) {
      const a = parseNums(v.arr, { max: 10 }), n = a.length, pos = Math.floor(+v.pos), F = [];
      if (!(pos >= -1 && pos < n)) throw new Error('Cycle index must be between -1 and ' + (n - 1) + '.');
      const nx = (i) => (i === -1 ? -1 : i + 1 < n ? i + 1 : pos);
      let slow = 0, fast = 0;
      const view = (m, cls) => { const tags = {}; if (slow >= 0) tags[slow] = 'slow'; if (fast >= 0) tags[fast] = (tags[fast] ? tags[fast] + '+' : '') + 'fast'; const marks = {}; if (slow >= 0) marks[slow] = cls || 'sel'; if (fast >= 0) marks[fast] = cls || 'hl'; F.push({ msg: m, rows: [cellsRow('nodes' + (pos >= 0 ? '   (last node → back to index ' + pos + ')' : '   (last node → None)'), a, marks, tags)] }); };
      view('slow and fast both start at the head.');
      for (let g = 0; g < 40; g++) {
        if (fast === -1 || nx(fast) === -1) { view('fast reached the end (None) → no cycle.'); return F; }
        slow = nx(slow); fast = nx(nx(fast));
        if (slow === fast) { view('slow and fast are on the SAME node → a cycle exists ✔', 'ok'); return F; }
        view('slow moves 1 step, fast moves 2 steps.');
      }
      return F;
    } };
};

/* ---------- recursion ---------- */
VIZ.rec = function () {
  return { title: 'Recursion: the call stack', inputs: [sel('fn', 'Function', [['fact', 'factorial(n)'], ['fib', 'fib(n)  (n ≤ 6)'], ['sd', 'sum_digits(n)']], 'fact'), txt('n', 'n', '4')],
    build: function (v) {
      let n = Math.floor(+v.n); const F = [], st = []; let calls = 0, maxd = 0;
      if (v.fn === 'fib' && !(n >= 0 && n <= 6)) throw new Error('For fib use 0 ≤ n ≤ 6 (the tree grows fast!).');
      if (!(n >= 0 && n <= 9999999)) throw new Error('Use a whole number n ≥ 0 (up to 7 digits).');
      if (v.fn === 'fact' && n > 12) throw new Error('For factorial use n ≤ 12.');
      const view = (m, cls) => F.push({ msg: m, rows: [stackRow('call stack (top = currently running)', st.slice(), cls || 'hl'), kvRow('stats', [{ k: 'calls so far', v: calls }, { k: 'max depth', v: maxd }])] });
      const name = v.fn === 'fact' ? 'fact' : v.fn === 'fib' ? 'fib' : 'sum_digits';
      function go(x) {
        calls++; st.push(name + '(' + x + ')'); maxd = Math.max(maxd, st.length);
        view('Call ' + name + '(' + x + ') - pushed on the stack.');
        let r;
        if (v.fn === 'fact') { if (x <= 1) r = 1; else r = x * go(x - 1); }
        else if (v.fn === 'fib') { if (x < 2) r = x; else r = go(x - 1) + go(x - 2); }
        else { if (x < 10) r = x; else r = (x % 10) + go(Math.floor(x / 10)); }
        view(name + '(' + x + ') returns ' + r + (((v.fn === 'fact' && x <= 1) || (v.fn === 'fib' && x < 2) || (v.fn === 'sd' && x < 10)) ? '   ← base case' : '') + ' - popped.', 'ok');
        st.pop(); return r;
      }
      view('Calling ' + name + '(' + n + ').');
      const res = go(n);
      F.push({ msg: 'Final answer: ' + name + '(' + n + ') = ' + res + '.  Total calls: ' + calls + ', deepest stack: ' + maxd + (v.fn === 'fib' ? '. Notice how many calls repeat the same work - that is why memoisation helps.' : '.'), rows: [stackRow('call stack', []), kvRow('result', [{ k: name + '(' + n + ')', v: res, cls: 'hl' }, { k: 'calls', v: calls }])] });
      return F;
    } };
};

VIZ.backtrack = function () {
  return { title: 'Backtracking: choose → explore → un-choose', inputs: [sel('mode', 'Problem', [['sub', 'Subsets'], ['perm', 'Permutations']], 'sub'), txt('arr', 'Items (≤ 4)', '1,2,3')],
    build: function (v) {
      const a = parseNums(v.arr, { max: 4 }); const F = [], path = [], res = [], used = a.map(() => false);
      const view = (m, cls) => F.push({ msg: m, rows: [cellsRow('current path', path.slice(), Object.fromEntries(path.map((_, i) => [i, cls || 'sel'])), {}, true), kvRow('results so far (' + res.length + ')', res.map((r) => ({ v: '[' + r.join(',') + ']' })))] });
      view('Path is empty.');
      if (v.mode === 'sub') {
        const go = (start) => {
          res.push(path.slice()); view('Record a copy of the path [' + path.join(', ') + '] - every path is a subset.', 'ok');
          for (let i = start; i < a.length; i++) { path.push(a[i]); view('Choose ' + a[i] + '.'); go(i + 1); const x = path.pop(); view('Un-choose ' + x + ' (backtrack).', 'bad'); }
        };
        go(0);
      } else {
        const go = () => {
          if (path.length === a.length) { res.push(path.slice()); view('Path is full → record permutation [' + path.join(', ') + '].', 'ok'); return; }
          for (let i = 0; i < a.length; i++) { if (used[i]) continue; used[i] = true; path.push(a[i]); view('Choose ' + a[i] + ' (mark used).'); go(); used[i] = false; const x = path.pop(); view('Un-choose ' + x + '.', 'bad'); }
        };
        go();
      }
      F.push({ msg: 'Done: ' + res.length + ' results (' + (v.mode === 'sub' ? '2^' + a.length : a.length + '!') + ').', rows: [kvRow('all results', res.map((r) => ({ v: '[' + r.join(',') + ']', cls: 'hl' })))] });
      return F;
    } };
};

VIZ.nqueens = function () {
  return { title: 'N-Queens backtracking', inputs: [sel('n', 'Board size n', [['4', '4 × 4'], ['5', '5 × 5'], ['6', '6 × 6']], '4')],
    build: function (v) {
      const n = +v.n, F = [], cols = new Array(n).fill(-1); let sols = 0, firstSol = null;
      const board = (m, hlRow, cls) => {
        const rows = [];
        for (let r = 0; r < n; r++) { const row = []; for (let c = 0; c < n; c++) row.push({ v: cols[r] === c ? '♛' : '', cls: cols[r] === c ? (r === hlRow ? cls || 'hl' : 'sel') : ((r + c) % 2 ? 'dim' : '') }); rows.push(row); }
        F.push({ msg: m, table: { rows: rows }, rows: [kvRow('solutions found', [{ v: sols, cls: sols ? 'hl' : '' }])] });
      };
      board('Empty board. Place one queen per row.');
      const safe = (r, c) => { for (let i = 0; i < r; i++) if (cols[i] === c || Math.abs(cols[i] - c) === r - i) return false; return true; };
      const go = (r) => {
        if (r === n) { sols++; if (!firstSol) firstSol = cols.slice(); board('All ' + n + ' queens placed → solution #' + sols + ' ✔', r - 1, 'ok'); return; }
        for (let c = 0; c < n; c++) {
          if (!safe(r, c)) continue;
          cols[r] = c; board('Row ' + r + ': column ' + c + ' is safe → place a queen.', r);
          go(r + 1);
          cols[r] = -1; if (r + 1 < n || true) board('Backtrack: remove the queen from row ' + r + ' and try the next column.', r - 1);
        }
      };
      go(0);
      board('Search finished. ' + sols + ' solution(s) for n = ' + n + '. Pruning skipped every attacked square.');
      return F;
    } };
};

/* ---------- trees ---------- */
function bstFrom(vals) {
  let root = null, id = 0;
  vals.forEach((x) => {
    const node = { val: x, l: null, r: null, id: id++ };
    if (!root) { root = node; return; }
    let c = root;
    for (;;) { if (x === c.val) return; if (x < c.val) { if (!c.l) { c.l = node; return; } c = c.l; } else { if (!c.r) { c.r = node; return; } c = c.r; } }
  });
  return root;
}
function treeLayout(root, gx, gy) {
  const nodes = [], edges = []; let counter = 0;
  (function walk(n, d, parent) {
    if (!n) return;
    walk(n.l, d + 1, n);
    n.x = 30 + counter++ * gx; n.y = 28 + d * gy; n.idx = nodes.length; nodes.push(n);
    walk(n.r, d + 1, n);
  })(root, 0, null);
  nodes.forEach((n) => { if (n.l) edges.push([n, n.l]); if (n.r) edges.push([n, n.r]); });
  return { nodes: nodes, edges: edges, w: 60 + nodes.length * gx, h: 56 + (Math.max(...nodes.map((n) => (n.y - 28) / gy)) + 0) * gy };
}
function treeSvg(root, cls, edgeOn, subs) {
  const L = treeLayout(root, 46, 62);
  const idxOf = new Map(L.nodes.map((n, i) => [n, i]));
  return { w: L.w, h: L.h + 20, nodes: L.nodes.map((n) => ({ x: n.x, y: n.y, label: n.val, cls: cls(n) || '', sub: subs ? subs(n) : '' })), edges: L.edges.map((e) => ({ a: idxOf.get(e[0]), b: idxOf.get(e[1]), cls: edgeOn && edgeOn(e) ? 'on' : '' })), r: 18 };
}
VIZ.tree = function (param) {
  return { title: 'Binary search tree traversals', inputs: [
    sel('mode', 'Operation', [['inorder', 'Inorder (L, node, R)'], ['preorder', 'Preorder (node, L, R)'], ['postorder', 'Postorder (L, R, node)'], ['level', 'Level order (BFS)'], ['search', 'BST search']], param || 'inorder'),
    txt('arr', 'Insert values in this order (BST)', '8,3,10,1,6,14,4,7'), txt('t', 'Search target (search mode)', '7')],
    build: function (v) {
      const vals = parseNums(v.arr, { max: 12 }); const root = bstFrom(vals); const F = [];
      const visited = new Set(); const order = [];
      const view = (m, cur, extra) => F.push({ msg: m, svg: treeSvg(root, (n) => (n === cur ? 'hl' : visited.has(n) ? 'ok' : ''), null), rows: [kvRow('visit order', order.map((x) => ({ v: x }))), extra].filter(Boolean) });
      view('This BST was built by inserting ' + vals.join(', ') + ' (left < node < right).');
      const m = v.mode;
      if (m === 'inorder' || m === 'preorder' || m === 'postorder') {
        const go = (n) => {
          if (!n) return;
          if (m === 'preorder') { visited.add(n); order.push(n.val); view('Visit ' + n.val + ' first (preorder).', n); }
          go(n.l);
          if (m === 'inorder') { visited.add(n); order.push(n.val); view('Left subtree done → visit ' + n.val + ' (inorder). The output is sorted!', n); }
          go(n.r);
          if (m === 'postorder') { visited.add(n); order.push(n.val); view('Both subtrees done → visit ' + n.val + ' (postorder).', n); }
        };
        go(root);
        view('Traversal complete: ' + order.join(' → ') + '.');
      } else if (m === 'level') {
        const q = [root];
        while (q.length) {
          const n = q.shift(); visited.add(n); order.push(n.val);
          if (n.l) q.push(n.l); if (n.r) q.push(n.r);
          view('Dequeue ' + n.val + ', visit it, enqueue its children.', n, kvRow('queue', q.map((x) => ({ v: x.val }))));
        }
        view('Level order complete: ' + order.join(' → ') + '.');
      } else {
        const t = +v.t; let c = root; const path = new Set();
        while (c) {
          path.add(c); visited.add(c);
          if (c.val === t) { view('Found ' + t + ' ✔ after ' + path.size + ' comparison(s).', c); return F; }
          view(t + (t < c.val ? ' < ' : ' > ') + c.val + ' → go ' + (t < c.val ? 'left' : 'right') + '.', c);
          c = t < c.val ? c.l : c.r;
        }
        view('Reached an empty spot: ' + t + ' is not in the tree. Search visited ' + path.size + ' node(s) - O(height).');
      }
      return F;
    } };
};

VIZ.heap = function () {
  return { title: 'Min / max heap', inputs: [sel('kind', 'Heap type', [['min', 'Min-heap'], ['max', 'Max-heap']], 'min'), sel('mode', 'Operations', [['ins', 'Insert values'], ['both', 'Insert, then extract all']], 'ins'), txt('arr', 'Values', '5,3,8,1,9,2')],
    build: function (v) {
      const vals = parseNums(v.arr, { max: 10 }), a = [], F = [];
      const better = (x, y) => (v.kind === 'min' ? x < y : x > y);
      const draw = (m, marks) => {
        const n = a.length, pos = a.map((_, i) => { const d = Math.floor(Math.log2(i + 1)); const first = Math.pow(2, d) - 1; const cnt = Math.pow(2, d); return { x: 0, y: 30 + d * 62, d: d, k: i - first, cnt: cnt }; });
        const W = 640;
        pos.forEach((p) => { p.x = (W / (p.cnt + 1)) * (p.k + 1); });
        const edges = []; a.forEach((_, i) => { if (i > 0) edges.push({ a: (i - 1) >> 1, b: i }); });
        F.push({ msg: m, svg: { w: W, h: 60 + (n ? pos[n - 1].d : 0) * 62, nodes: a.map((x, i) => ({ x: pos[i].x, y: pos[i].y, label: x, cls: marks && marks[i] || '', sub: '' })), edges: edges, r: 18 }, rows: [cellsRow('array form (children of i are 2i+1 and 2i+2)', a.slice(), marks || {}, {})] });
      };
      draw('Empty heap. Root must always be the ' + (v.kind === 'min' ? 'smallest' : 'largest') + ' value.');
      vals.forEach((x) => {
        a.push(x); let i = a.length - 1; draw('Insert ' + x + ' at the end (keeps the tree complete).', { [i]: 'hl' });
        while (i > 0 && better(a[i], a[(i - 1) >> 1])) { const p = (i - 1) >> 1; draw(a[i] + ' is ' + (v.kind === 'min' ? 'smaller' : 'larger') + ' than its parent ' + a[p] + ' → swap (sift up).', { [i]: 'hl', [p]: 'sel' }); const t = a[i]; a[i] = a[p]; a[p] = t; i = p; draw('Swapped.', { [i]: 'ok' }); }
      });
      draw('Heap built by ' + vals.length + ' inserts (each O(log n)). Root = ' + a[0] + '.', { 0: 'ok' });
      if (v.mode === 'both') {
        const out = [];
        while (a.length) {
          const top = a[0]; out.push(top); const last = a.pop();
          if (a.length) { a[0] = last; draw('Extract ' + top + ': move the last element (' + last + ') to the root, then sift down.', { 0: 'hl' }); let i = 0; for (;;) { let b = i; const l = 2 * i + 1, r = 2 * i + 2; if (l < a.length && better(a[l], a[b])) b = l; if (r < a.length && better(a[r], a[b])) b = r; if (b === i) break; draw('Swap ' + a[i] + ' with its ' + (v.kind === 'min' ? 'smaller' : 'larger') + ' child ' + a[b] + '.', { [i]: 'hl', [b]: 'sel' }); const t = a[i]; a[i] = a[b]; a[b] = t; i = b; } draw('Heap property restored. Extracted so far: ' + out.join(', '), { 0: 'ok' }); } else draw('Extracted last element ' + top + '. Order out: ' + out.join(', ') + ' (sorted - this is heap sort!).');
        }
      }
      return F;
    } };
};

/* ---------- graphs ---------- */
function parseEdges(str, directed, weighted) {
  const parts = String(str).split(/[,;\n]+/).map((x) => x.trim()).filter(Boolean);
  if (!parts.length || parts.length > 18) throw new Error('Enter 1 to 18 edges, e.g. A-B, B-C' + (weighted ? '-3' : '') + '.');
  const names = new Set(), edges = [];
  parts.forEach((p) => {
    const m = p.match(directed ? /^([A-Za-z0-9]+)\s*->\s*([A-Za-z0-9]+)$/ : /^([A-Za-z0-9]+)\s*-\s*([A-Za-z0-9]+)(?:\s*-\s*(\d+))?$/);
    if (!m) throw new Error('Bad edge "' + p + '". Use ' + (directed ? 'A->B' : 'A-B or A-B-4 (weight)') + '.');
    names.add(m[1]); names.add(m[2]); edges.push([m[1], m[2], m[3] ? +m[3] : null]);
  });
  const list = Array.from(names).sort();
  if (list.length > 10) throw new Error('Please use at most 10 nodes.');
  return { names: list, edges: edges };
}
VIZ.graph = function (param) {
  return { title: 'Graph traversal and shortest paths', inputs: [
    sel('algo', 'Algorithm', [['bfs', 'BFS (queue)'], ['dfs', 'DFS (recursion / stack)'], ['dijkstra', 'Dijkstra (min-heap)']], param || 'bfs'),
    { id: 'edges', label: 'Undirected edges  (A-B or A-B-weight)', type: 'text', value: 'A-B-4, A-C-2, B-C-1, B-D-5, C-E-8, D-F-3, E-G-2, E-F-1, F-G-4' }, txt('start', 'Start node', 'A')],
    build: function (v) {
      const g = parseEdges(v.edges, false, true), names = g.names, F = [];
      if (!names.includes(v.start.trim())) throw new Error('Start node must be one of: ' + names.join(', '));
      const pos = layoutCircle(names.length, 560, 320), id = (nm) => names.indexOf(nm);
      const adj = names.map(() => []);
      g.edges.forEach(([a, b, w]) => { adj[id(a)].push([id(b), w === null ? 1 : w]); adj[id(b)].push([id(a), w === null ? 1 : w]); });
      adj.forEach((l) => l.sort((x, y) => x[0] - y[0]));
      const weighted = g.edges.some((e) => e[2] !== null);
      const cls = new Array(names.length).fill(''), subs = new Array(names.length).fill('');
      const onEdges = new Set(); const ek = (a, b) => Math.min(a, b) + '-' + Math.max(a, b);
      const svg = () => ({ w: 560, h: 320, r: 20, nodes: names.map((nm, i) => ({ x: pos[i].x, y: pos[i].y, label: nm, cls: cls[i], sub: subs[i] })), edges: g.edges.map(([a, b, w]) => ({ a: id(a), b: id(b), label: weighted && w !== null ? w : '', cls: onEdges.has(ek(id(a), id(b))) ? 'on' : '' })) });
      const s0 = id(v.start.trim()); const algo = v.algo;
      if (algo === 'bfs') {
        const vis = new Set([s0]), q = [s0], order = [];
        cls[s0] = 'sel';
        const view = (m) => F.push({ msg: m, svg: svg(), rows: [cellsRow('queue (front → back)', q.map((x) => names[x]), {}, {}, true), kvRow('visit order', order.map((x) => ({ v: names[x] })))], legend: [['var(--hl)', 'being processed'], ['var(--sel)', 'in queue'], ['var(--done)', 'finished']] });
        view('Start: enqueue ' + names[s0] + ' and mark it visited.');
        while (q.length) {
          const u = q.shift(); order.push(u); cls[u] = 'hl';
          view('Dequeue ' + names[u] + ' and look at its neighbours.');
          const added = [];
          adj[u].forEach(([w]) => { if (!vis.has(w)) { vis.add(w); q.push(w); cls[w] = 'sel'; onEdges.add(ek(u, w)); added.push(names[w]); } });
          cls[u] = 'ok';
          view(added.length ? 'Enqueue unvisited neighbours: ' + added.join(', ') + '.' : names[u] + ' has no unvisited neighbours.');
        }
        view('Queue empty → BFS finished: ' + order.map((x) => names[x]).join(' → ') + '. Highlighted edges form the BFS tree (shortest paths in edges).');
      } else if (algo === 'dfs') {
        const vis = new Set(), stk = [], order = [];
        const view = (m) => F.push({ msg: m, svg: svg(), rows: [stackRow('recursion stack (top = current)', stk.map((x) => names[x])), kvRow('visit order', order.map((x) => ({ v: names[x] })))], legend: [['var(--hl)', 'current'], ['var(--sel)', 'on the stack'], ['var(--done)', 'finished']] });
        view('DFS goes as deep as possible before backing up.');
        const go = (u, parent) => {
          vis.add(u); stk.push(u); order.push(u); cls[u] = 'hl'; if (parent !== null) onEdges.add(ek(u, parent));
          view('Visit ' + names[u] + ' (push on the stack).');
          for (const [w] of adj[u]) { if (!vis.has(w)) { cls[u] = 'sel'; go(w, u); cls[u] = 'hl'; view('Back at ' + names[u] + ': check the next neighbour.'); } }
          stk.pop(); cls[u] = 'ok'; view(names[u] + ' fully explored → pop.');
        };
        go(s0, null);
        view('DFS finished: ' + order.map((x) => names[x]).join(' → ') + '.');
      } else {
        const dist = new Array(names.length).fill(Infinity); dist[s0] = 0; let heap = [[0, s0]]; const done = new Set(); const parent = new Array(names.length).fill(-1);
        const dv = () => kvRow('shortest distance so far', names.map((nm, i) => ({ k: nm, v: dist[i] === Infinity ? '∞' : dist[i], cls: done.has(i) ? 'hl' : '' })));
        names.forEach((_, i) => { subs[i] = i === s0 ? '0' : '∞'; });
        const view = (m) => F.push({ msg: m, svg: svg(), rows: [dv(), cellsRow('min-heap (distance, node)', heap.slice().sort((x, y) => x[0] - y[0]).map((x) => '(' + x[0] + ',' + names[x[1]] + ')'), {}, {}, true)], legend: [['var(--hl)', 'popped / finalised'], ['var(--sel)', 'in heap'], ['var(--done)', 'finished']] });
        cls[s0] = 'sel'; view('dist[' + names[s0] + '] = 0, everything else ∞. Push (0, ' + names[s0] + ').');
        while (heap.length) {
          heap.sort((x, y) => x[0] - y[0]); const [d, u] = heap.shift();
          if (done.has(u)) { view('Skip stale entry (' + d + ', ' + names[u] + ') - already finalised.'); continue; }
          done.add(u); cls[u] = 'hl'; if (parent[u] >= 0) onEdges.add(ek(u, parent[u]));
          view('Pop the closest node ' + names[u] + ' (distance ' + d + ') - its distance is now final.');
          const ups = [];
          adj[u].forEach(([w, wt]) => { if (!done.has(w) && d + wt < dist[w]) { dist[w] = d + wt; parent[w] = u; heap.push([dist[w], w]); cls[w] = 'sel'; subs[w] = String(dist[w]); ups.push(names[w] + '=' + dist[w]); } });
          cls[u] = 'ok'; subs[u] = String(d);
          view(ups.length ? 'Relax edges from ' + names[u] + ': improved ' + ups.join(', ') + '.' : 'No improvements through ' + names[u] + '.');
        }
        view('Heap empty → Dijkstra finished. Highlighted edges form the shortest-path tree. Requires non-negative weights.');
      }
      return F;
    } };
};

VIZ.grid = function () {
  return { title: 'Grid BFS: shortest path in a maze', note: 'S = start, E = end, # = wall, . = open', inputs: [{ id: 'g', label: 'Grid (edit me!)', type: 'textarea', rows: 6, value: 'S..#....\n.#.#.##.\n.#...#..\n.####.#.\n......#E' }],
    build: function (v) {
      const rows = String(v.g).split('\n').map((r) => r.trim()).filter(Boolean);
      if (!rows.length || rows.length > 9 || rows.some((r) => r.length !== rows[0].length || r.length > 12 || /[^.#SE]/.test(r))) throw new Error('Use up to 9 rows of equal length (max 12) with only . # S E');
      const R = rows.length, C = rows[0].length; let sr = -1, sc = -1, er = -1, ec = -1;
      rows.forEach((r, i) => r.split('').forEach((ch, j) => { if (ch === 'S') { sr = i; sc = j; } if (ch === 'E') { er = i; ec = j; } }));
      if (sr < 0 || er < 0) throw new Error('The grid needs one S and one E.');
      const dist = rows.map(() => new Array(C).fill(-1)), par = rows.map(() => new Array(C).fill(null)); dist[sr][sc] = 0;
      const F = [];
      const frame = (m, front, path) => {
        const tab = rows.map((r, i) => r.split('').map((ch, j) => {
          let cls = '', val = dist[i][j] >= 0 ? dist[i][j] : '';
          if (ch === '#') { cls = 'wall'; val = ''; } else if (dist[i][j] >= 0) cls = 'sel';
          if (front && front.some((p) => p[0] === i && p[1] === j)) cls = 'hl';
          if (path && path.has(i + ',' + j)) cls = 'ok';
          if (ch === 'S') { val = 'S'; if (cls === 'sel') cls = 'pv'; } if (ch === 'E') { val = 'E'; if (!cls) cls = 'dim'; }
          return { v: val, cls: cls };
        }));
        F.push({ msg: m, table: { rows: tab }, legend: [['var(--hl)', 'current wave-front'], ['var(--sel)', 'visited (number = distance)'], ['var(--done)', 'shortest path'], ['var(--code-bg)', 'wall']] });
      };
      frame('Distance 0: the start cell. BFS expands one "ring" of cells at a time.', [[sr, sc]]);
      let wave = [[sr, sc]], d = 0, found = false;
      while (wave.length && !found) {
        const nxt = [];
        for (const [r, c] of wave) for (const [dr, dc] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
          const nr = r + dr, nc = c + dc;
          if (nr < 0 || nc < 0 || nr >= R || nc >= C || rows[nr][nc] === '#' || dist[nr][nc] >= 0) continue;
          dist[nr][nc] = d + 1; par[nr][nc] = [r, c]; nxt.push([nr, nc]);
          if (nr === er && nc === ec) found = true;
        }
        d++; wave = nxt;
        if (wave.length) frame('Distance ' + d + ': ' + wave.length + ' new cell(s) reached.' + (found ? ' The end cell E is reached!' : ''), wave);
      }
      if (!found) { frame('The queue is empty and E was never reached → no path (-1).'); return F; }
      const path = new Set(); let p = [er, ec]; while (p) { path.add(p[0] + ',' + p[1]); p = par[p[0]][p[1]]; }
      frame('Shortest path length = ' + dist[er][ec] + ' moves. Follow the parent links back from E to S.', null, path);
      return F;
    } };
};

VIZ.topo = function () {
  return { title: "Topological sort (Kahn's algorithm)", inputs: [{ id: 'edges', label: 'Directed edges  (A->B means A before B)', type: 'text', value: 'A->C, B->C, B->D, C->E, D->F, E->F' }],
    build: function (v) {
      const g = parseEdges(v.edges, true), names = g.names, id = (x) => names.indexOf(x), F = [];
      const adj = names.map(() => []), indeg = names.map(() => 0);
      g.edges.forEach(([a, b]) => { adj[id(a)].push(id(b)); indeg[id(b)]++; });
      const pos = layoutCircle(names.length, 560, 320), cls = names.map(() => ''), q = [], order = [];
      names.forEach((_, i) => { if (!indeg[i]) { q.push(i); cls[i] = 'sel'; } });
      const view = (m) => F.push({ msg: m, svg: { w: 560, h: 320, r: 20, nodes: names.map((nm, i) => ({ x: pos[i].x, y: pos[i].y, label: nm, cls: cls[i], sub: 'in ' + indeg[i] })), edges: g.edges.map(([a, b]) => ({ a: id(a), b: id(b), dir: true, cls: '' })) }, rows: [kvRow('in-degrees', names.map((nm, i) => ({ k: nm, v: indeg[i] }))), cellsRow('queue (in-degree 0)', q.map((x) => names[x]), {}, {}, true), cellsRow('topological order so far', order.map((x) => names[x]), Object.fromEntries(order.map((_, i) => [i, 'ok'])), {}, true)] });
      view('Compute in-degrees (number of prerequisites). Nodes with in-degree 0 can go first.');
      while (q.length) {
        const u = q.shift(); order.push(u); cls[u] = 'hl'; view('Take ' + names[u] + ' → add to the order and remove its outgoing edges.');
        adj[u].forEach((w) => { indeg[w]--; if (!indeg[w]) { q.push(w); cls[w] = 'sel'; } });
        cls[u] = 'ok'; view('Decrease the in-degree of ' + (adj[u].map((x) => names[x]).join(', ') || 'nobody') + '; any node reaching 0 joins the queue.');
      }
      F.push({ msg: order.length === names.length ? 'All ' + names.length + ' nodes ordered ✔  ' + order.map((x) => names[x]).join(' → ') : 'Only ' + order.length + ' of ' + names.length + ' nodes could be ordered → the graph has a CYCLE, no valid order exists.', svg: F[F.length - 1].svg, rows: F[F.length - 1].rows });
      return F;
    } };
};

VIZ.dsu = function () {
  return { title: 'Union-Find (disjoint sets)', inputs: [txt('n', 'Number of elements', '7'), txt('ops', 'Union operations (a-b, ...)', '0-1, 2-3, 1-3, 4-5, 0-2, 5-6')],
    build: function (v) {
      const n = Math.floor(+v.n); if (!(n >= 2 && n <= 10)) throw new Error('Use 2 to 10 elements.');
      const ops = String(v.ops).split(/[,;]+/).map((x) => x.trim()).filter(Boolean).map((p) => { const m = p.match(/^(\d+)\s*-\s*(\d+)$/); if (!m || +m[1] >= n || +m[2] >= n) throw new Error('Bad operation "' + p + '". Use numbers below ' + n + ' like 0-1.'); return [+m[1], +m[2]]; });
      const par = range(0, n - 1), size = new Array(n).fill(1); let groups = n; const F = [];
      const find = (x) => { while (par[x] !== x) { par[x] = par[par[x]]; x = par[x]; } return x; };
      const view = (m, hl) => F.push({ msg: m, rows: [cellsRow('parent[]  (parent[i] == i means i is a root)', par.slice(), Object.fromEntries(par.map((p, i) => [i, p === i ? 'ok' : ''])), Object.fromEntries((hl || []).map((x) => [x, '▲']))), cellsRow('size of tree (valid at roots)', size.slice(), {}, {}), kvRow('stats', [{ k: 'groups', v: groups, cls: 'hl' }])] });
      view('Every element starts as its own group (its own root).');
      ops.forEach(([a, b]) => {
        const ra = find(a), rb = find(b);
        if (ra === rb) { view('union(' + a + ', ' + b + '): both already have root ' + ra + ' → already connected. In an edge list this edge would close a CYCLE.', [a, b]); return; }
        let x = ra, y = rb; if (size[x] < size[y]) { const t = x; x = y; y = t; }
        par[y] = x; size[x] += size[y]; groups--;
        view('union(' + a + ', ' + b + '): roots ' + ra + ' and ' + rb + ' differ → attach root ' + y + ' under root ' + x + ' (smaller under larger).', [y]);
      });
      view('Final: ' + groups + ' group(s). find() with path compression keeps trees almost flat → near O(1).');
      return F;
    } };
};

VIZ.trie = function () {
  return { title: 'Trie (prefix tree)', inputs: [txt('words', 'Words to insert', 'tea,ten,to,inn,in'), txt('q', 'Query (word or prefix)', 'te')],
    build: function (v) {
      const words = String(v.words).split(/[\s,]+/).filter(Boolean).map((w) => w.toLowerCase()); if (!words.length || words.length > 7 || words.some((w) => !/^[a-z]{1,6}$/.test(w))) throw new Error('Enter up to 7 words (letters a-z, ≤ 6 letters each).');
      const mkNode = (ch, parent) => ({ ch: ch, kids: {}, end: false, parent: parent, id: 0 });
      // pass 1: build the final trie to fix the layout
      const root = mkNode('root', null); const all = [root];
      const ins = (word, rt, out) => { let n = rt; for (const ch of word) { if (!n.kids[ch]) { n.kids[ch] = mkNode(ch, n); if (out) out.push(n.kids[ch]); } n = n.kids[ch]; } n.end = true; return n; };
      words.forEach((w) => ins(w, root, all)); all.forEach((n, i) => { n.id = i; });
      let leaf = 0; const place = (n, d) => { const ks = Object.keys(n.kids).sort(); if (!ks.length) n.x = 30 + leaf++ * 46; else { ks.forEach((k) => place(n.kids[k], d + 1)); n.x = (n.kids[ks[0]].x + n.kids[ks[ks.length - 1]].x) / 2; } n.y = 28 + d * 56; }; place(root, 0);
      const W = 60 + leaf * 46, H = 56 + Math.max(...all.map((n) => (n.y - 28) / 56)) * 56 + 20;
      const present = new Set([0]); const ends = new Set(); const hl = new Set(); const pathSet = new Set(); const F = [];
      const view = (m, cur) => F.push({ msg: m, svg: { w: Math.max(W, 120), h: H, r: 17, nodes: all.map((n) => ({ x: n.x, y: n.y, label: n.id === 0 ? '•' : n.ch, hidden: !present.has(n.id), cls: n.id === cur ? 'hl' : pathSet.has(n.id) ? 'sel' : ends.has(n.id) ? 'ok' : '', sub: '' })), edges: all.filter((n) => n.parent && present.has(n.id)).map((n) => ({ a: n.parent.id, b: n.id, cls: pathSet.has(n.id) ? 'on' : '' })) }, legend: [['var(--done)', 'end of a stored word'], ['var(--hl)', 'current'], ['var(--sel)', 'queried path']] });
      view('Empty trie: just the root.');
      words.forEach((w) => {
        let n = root;
        for (const ch of w) { n = n.kids[ch]; const was = present.has(n.id); present.add(n.id); view((was ? 'Reuse existing node ' : 'Create new node ') + "'" + ch + "' while inserting \"" + w + '".', n.id); }
        ends.add(n.id); view('Mark \'' + w + '\' as a complete word (green node).', n.id);
      });
      const q = String(v.q).trim().toLowerCase();
      if (q) {
        let n = root, ok = true;
        for (const ch of q) { if (!n.kids[ch]) { ok = false; view("No child '" + ch + "' → \"" + q + '" is not in the trie.'); break; } n = n.kids[ch]; pathSet.add(n.id); view("Follow '" + ch + "'.", n.id); }
        if (ok) view('Path exists → "' + q + '" IS a prefix. It ' + (n.end ? 'is also a stored word ✔' : 'is not itself a stored word (no green end marker).'));
      }
      return F;
    } };
};

/* ---------- DP ---------- */
VIZ.dp = function (param) {
  const PRE = {
    fib: { a: '9', b: '', c: '' }, coin: { a: '1,3,4', b: '6', c: '' }, robber: { a: '2,7,9,3,1', b: '', c: '' }, paths: { a: '4', b: '5', c: '' },
    lcs: { a: 'abcde', b: 'ace', c: '' }, knap: { a: '1,3,4,5', b: '1,4,5,7', c: '7' },
  };
  const LAB = { fib: ['n (≤ 15)', '', ''], coin: ['coins', 'amount (≤ 18)', ''], robber: ['house values', '', ''], paths: ['rows m (≤ 6)', 'cols n (≤ 7)', ''], lcs: ['string A (≤ 7)', 'string B (≤ 7)', ''], knap: ['weights', 'values', 'capacity (≤ 10)'] };
  const presets = {}; Object.keys(PRE).forEach((k) => { presets[k] = PRE[k]; });
  const p = param || 'fib';
  return { title: 'Dynamic programming tables', inputs: [
    sel('prob', 'Problem', [['fib', 'Fibonacci / climbing stairs'], ['coin', 'Coin change (min coins)'], ['robber', 'House robber'], ['paths', 'Unique grid paths'], ['lcs', 'Longest common subsequence'], ['knap', '0/1 knapsack']], p, presets),
    Object.assign(txt('a', LAB[p][0], PRE[p].a), { label_fn: (vv) => LAB[vv.prob][0], show_fn: () => true }),
    Object.assign(txt('b', LAB[p][1] || 'unused', PRE[p].b), { label_fn: (vv) => LAB[vv.prob][1] || 'unused', show_fn: (vv) => !!LAB[vv.prob][1] }),
    Object.assign(txt('c', LAB[p][2] || 'unused', PRE[p].c), { label_fn: (vv) => LAB[vv.prob][2] || 'unused', show_fn: (vv) => !!LAB[vv.prob][2] })],
    build: function (v) {
      const F = [];
      const legend = [['var(--hl)', 'cell being computed'], ['var(--sel)', 'cells it depends on'], ['var(--done)', 'already filled']];
      if (v.prob === 'fib') {
        const n = Math.floor(+v.a); if (!(n >= 1 && n <= 15)) throw new Error('n must be between 1 and 15.');
        const dp = new Array(n + 1).fill(null); const show = (m, cur, deps) => F.push({ msg: m, table: { head: range(0, n), corner: 'i', rows: [dp.map((x, i) => ({ v: x === null ? '' : x, cls: i === cur ? 'hl' : deps && deps.includes(i) ? 'sel' : x !== null ? 'ok' : '' }))], side: ['dp[i]'] }, legend: legend });
        dp[0] = 0; dp[1] = 1; show('Base cases: dp[0] = 0, dp[1] = 1 (state: dp[i] = i-th Fibonacci number).');
        for (let i = 2; i <= n; i++) { dp[i] = dp[i - 1] + dp[i - 2]; show('dp[' + i + '] = dp[' + (i - 1) + '] + dp[' + (i - 2) + '] = ' + dp[i - 1] + ' + ' + dp[i - 2] + ' = ' + dp[i] + '.   (Same recurrence solves "climbing stairs" with dp[1]=1, dp[2]=2.)', i, [i - 1, i - 2]); }
        show('Answer: fib(' + n + ') = ' + dp[n] + '. Time O(n), space O(n) (O(1) with two variables).', n);
      } else if (v.prob === 'coin') {
        const coins = parseNums(v.a, { max: 5, int: true, min: 1 }), amt = Math.floor(+v.b); if (!(amt >= 1 && amt <= 18)) throw new Error('Amount must be between 1 and 18.');
        const dp = new Array(amt + 1).fill(null); dp[0] = 0;
        const show = (m, cur, deps) => F.push({ msg: m, table: { head: range(0, amt), corner: 'amount', rows: [dp.map((x, i) => ({ v: x === null ? '' : x === Infinity ? '∞' : x, cls: i === cur ? 'hl' : deps && deps.includes(i) ? 'sel' : x !== null ? 'ok' : '' }))], side: ['min coins'] }, legend: legend });
        show('dp[a] = fewest coins to make amount a. dp[0] = 0. Coins: ' + coins.join(', ') + '.');
        for (let a = 1; a <= amt; a++) {
          let best = Infinity; const deps = [], parts = [];
          coins.forEach((c) => { if (c <= a) { const cand = dp[a - c] + 1; parts.push('coin ' + c + ' → dp[' + (a - c) + '] + 1 = ' + (cand === Infinity ? '∞' : cand)); if (cand < best) { best = cand; } } });
          coins.forEach((c) => { if (c <= a && dp[a - c] + 1 === best) deps.push(a - c); });
          dp[a] = best; show('dp[' + a + ']: ' + (parts.join(';  ') || 'no coin fits') + '  →  min = ' + (best === Infinity ? '∞ (impossible)' : best) + '.', a, deps);
        }
        show(dp[amt] === Infinity ? 'Amount ' + amt + ' cannot be made → return -1.' : 'Answer: ' + dp[amt] + ' coin(s). (Greedy would not always find this - try coins 1,3,4 and amount 6.)', amt);
      } else if (v.prob === 'robber') {
        const nums = parseNums(v.a, { max: 10, int: true, min: 0 }), n = nums.length, dp = new Array(n).fill(null);
        const show = (m, cur, deps) => F.push({ msg: m, table: { head: range(0, n - 1), corner: 'house', rows: [nums.map((x) => ({ v: x })), dp.map((x, i) => ({ v: x === null ? '' : x, cls: i === cur ? 'hl' : deps && deps.includes(i) ? 'sel' : x !== null ? 'ok' : '' }))], side: ['money', 'best so far'] }, legend: legend });
        show('dp[i] = best total using houses 0..i with no two adjacent.');
        for (let i = 0; i < n; i++) {
          if (i === 0) { dp[0] = nums[0]; show('dp[0] = nums[0] = ' + nums[0] + '.', 0); } else if (i === 1) { dp[1] = Math.max(nums[0], nums[1]); show('dp[1] = max(' + nums[0] + ', ' + nums[1] + ') = ' + dp[1] + '.', 1, [0]); } else { const skip = dp[i - 1], take = dp[i - 2] + nums[i]; dp[i] = Math.max(skip, take); show('dp[' + i + '] = max(skip: dp[' + (i - 1) + '] = ' + skip + ', rob: dp[' + (i - 2) + '] + ' + nums[i] + ' = ' + take + ') = ' + dp[i] + '.', i, [i - 1, i - 2]); }
        }
        show('Answer: ' + dp[n - 1] + '.', n - 1);
      } else if (v.prob === 'paths') {
        const m = Math.floor(+v.a), n = Math.floor(+v.b); if (!(m >= 1 && m <= 6 && n >= 1 && n <= 7)) throw new Error('Use rows 1-6 and columns 1-7.');
        const dp = range(1, m).map(() => new Array(n).fill(null));
        const show = (mm, r, c) => F.push({ msg: mm, table: { head: range(0, n - 1), corner: '', side: range(0, m - 1), rows: dp.map((row, i) => row.map((x, j) => ({ v: x === null ? '' : x, cls: i === r && j === c ? 'hl' : (i === r - 1 && j === c) || (i === r && j === c - 1) ? 'sel' : x !== null ? 'ok' : '' }))) }, legend: legend });
        show('paths[r][c] = ways to reach cell (r, c) moving only right or down.');
        for (let r = 0; r < m; r++) for (let c = 0; c < n; c++) { dp[r][c] = r === 0 || c === 0 ? 1 : dp[r - 1][c] + dp[r][c - 1]; show(r === 0 || c === 0 ? 'First row/column: only one way (all right or all down) → 1.' : 'paths[' + r + '][' + c + '] = from above ' + dp[r - 1][c] + ' + from left ' + dp[r][c - 1] + ' = ' + dp[r][c] + '.', r, c); }
        show('Answer: ' + dp[m - 1][n - 1] + ' paths.', m - 1, n - 1);
      } else if (v.prob === 'lcs') {
        const A = parseStr(v.a, 7), B = parseStr(v.b, 7), dp = range(0, A.length).map(() => new Array(B.length + 1).fill(null));
        for (let i = 0; i <= A.length; i++) dp[i][0] = 0; for (let j = 0; j <= B.length; j++) dp[0][j] = 0;
        const show = (m, r, c, deps) => F.push({ msg: m, table: { head: [''].concat(B.split('')), corner: '', side: [''].concat(A.split('')), rows: dp.map((row, i) => row.map((x, j) => ({ v: x === null ? '' : x, cls: i === r && j === c ? 'hl' : deps && deps.some((d) => d[0] === i && d[1] === j) ? 'sel' : x !== null ? 'ok' : '' }))) }, legend: legend });
        show('dp[i][j] = LCS length of the first i letters of A and first j letters of B. Row 0 / column 0 = empty string = 0.');
        for (let i = 1; i <= A.length; i++) for (let j = 1; j <= B.length; j++) {
          if (A[i - 1] === B[j - 1]) { dp[i][j] = dp[i - 1][j - 1] + 1; show("'" + A[i - 1] + "' = '" + B[j - 1] + "' match → dp[" + i + '][' + j + '] = dp[' + (i - 1) + '][' + (j - 1) + '] + 1 = ' + dp[i][j] + '.', i, j, [[i - 1, j - 1]]); } else { dp[i][j] = Math.max(dp[i - 1][j], dp[i][j - 1]); show("'" + A[i - 1] + "' ≠ '" + B[j - 1] + "' → dp[" + i + '][' + j + '] = max(above ' + dp[i - 1][j] + ', left ' + dp[i][j - 1] + ') = ' + dp[i][j] + '.', i, j, [[i - 1, j], [i, j - 1]]); }
        }
        show('Answer: LCS length = ' + dp[A.length][B.length] + '.', A.length, B.length);
      } else {
        const W = parseNums(v.a, { max: 5, int: true, min: 1 }), Vv = parseNums(v.b, { max: 5, int: true, min: 0 }), cap = Math.floor(+v.c);
        if (W.length !== Vv.length) throw new Error('Weights and values need the same count.'); if (!(cap >= 1 && cap <= 10)) throw new Error('Capacity must be 1-10.');
        const dp = range(0, W.length).map(() => new Array(cap + 1).fill(null)); for (let w = 0; w <= cap; w++) dp[0][w] = 0;
        const show = (m, r, c, deps) => F.push({ msg: m, table: { head: range(0, cap), corner: 'cap →', side: ['no items'].concat(W.map((w, i) => 'item ' + (i + 1) + ' (w' + w + ',v' + Vv[i] + ')')), rows: dp.map((row, i) => row.map((x, j) => ({ v: x === null ? '' : x, cls: i === r && j === c ? 'hl' : deps && deps.some((d) => d[0] === i && d[1] === j) ? 'sel' : x !== null ? 'ok' : '' }))) }, legend: legend });
        show('dp[i][w] = best value using the first i items with capacity w. Row 0 = no items = 0.');
        for (let i = 1; i <= W.length; i++) for (let w = 0; w <= cap; w++) {
          const skip = dp[i - 1][w]; let m = 'dp[' + i + '][' + w + ']: skip item ' + i + ' → ' + skip;
          if (w >= W[i - 1]) { const take = dp[i - 1][w - W[i - 1]] + Vv[i - 1]; dp[i][w] = Math.max(skip, take); m += '; take it → dp[' + (i - 1) + '][' + (w - W[i - 1]) + '] + ' + Vv[i - 1] + ' = ' + take; show(m + '  → max = ' + dp[i][w] + '.', i, w, [[i - 1, w], [i - 1, w - W[i - 1]]]); } else { dp[i][w] = skip; show(m + ' (item is too heavy) → ' + skip + '.', i, w, [[i - 1, w]]); }
        }
        show('Answer: maximum value = ' + dp[W.length][cap] + '.', W.length, cap);
      }
      return F;
    } };
};

/* ---------- bits (live) ---------- */
VIZ.bits = function () {
  return { live: function (host) {
    host.className = 'viz'; host.innerHTML = '';
    let A = 13, B = 11;
    const stage = h('div', { class: 'stage' });
    const bin = (x) => (x >>> 0 & 255).toString(2).padStart(8, '0');
    function bitsRow(label, val, which) {
      const bs = bin(val).split('');
      const row = h('div', { class: 'row' }, h('div', { class: 'rl', text: label + ' = ' + val }));
      const c = h('div', { class: 'cells' });
      bs.forEach((b, i) => {
        const pos = 7 - i;
        const el = which ? h('button', { class: 'cell ' + (b === '1' ? 'sel' : ''), text: b, 'aria-label': 'Toggle bit ' + pos + ' of ' + which, onclick: () => { if (which === 'a') A ^= (1 << pos); else B ^= (1 << pos); draw(); } }) : h('div', { class: 'cell ' + (b === '1' ? 'ok' : ''), text: b });
        c.appendChild(h('div', { class: 'cellbox' }, el, h('div', { class: 'idx', text: '2^' + pos })));
      });
      row.appendChild(c); return row;
    }
    function draw() {
      stage.innerHTML = '';
      stage.appendChild(h('div', { class: 'tip', text: 'Click any bit of A or B to flip it. Python integers are unbounded; this demo shows 8 bits.' }));
      stage.appendChild(bitsRow('A', A, 'a')); stage.appendChild(bitsRow('B', B, 'b'));
      stage.appendChild(bitsRow('A & B  (AND: both 1)', A & B)); stage.appendChild(bitsRow('A | B  (OR: either 1)', A | B)); stage.appendChild(bitsRow('A ^ B  (XOR: bits differ)', A ^ B));
      stage.appendChild(bitsRow('~A & 255  (NOT, 8-bit view; Python gives ' + (~A) + ')', ~A & 255));
      stage.appendChild(bitsRow('A << 1  (× 2)', (A << 1) & 255)); stage.appendChild(bitsRow('A >> 1  (÷ 2, floor)', A >> 1));
      const pc = bin(A).split('').filter((x) => x === '1').length;
      stage.appendChild(h('div', { class: 'callout', html: 'A is <b>' + (A & 1 ? 'odd' : 'even') + '</b> (A & 1 = ' + (A & 1) + '). Set bits: <b>' + pc + '</b>. Power of two? <b>' + (A > 0 && (A & (A - 1)) === 0 ? 'yes' : 'no') + '</b> (A & (A−1) = ' + (A & (A - 1)) + '). Lowest set bit: A & −A = <b>' + (A & -A) + '</b>.' }));
    }
    host.appendChild(h('header', null, h('b', { text: 'Bitwise calculator' })));
    const na = h('input', { type: 'number', value: A, min: 0, max: 255, 'aria-label': 'Number A', style: 'width:90px' });
    const nb = h('input', { type: 'number', value: B, min: 0, max: 255, 'aria-label': 'Number B', style: 'width:90px' });
    const sync = () => { A = Math.min(255, Math.max(0, Math.floor(+na.value) || 0)); B = Math.min(255, Math.max(0, Math.floor(+nb.value) || 0)); draw(); };
    na.addEventListener('input', sync); nb.addEventListener('input', sync);
    host.appendChild(h('div', { class: 'inputs' }, h('label', null, h('span', { text: 'A (0-255)' }), na), h('label', null, h('span', { text: 'B (0-255)' }), nb)));
    host.appendChild(stage);
    draw();
    const redraw = draw; draw = function () { redraw(); na.value = A; nb.value = B; }; // keep inputs in sync after clicks
  } };
};

VIZ.kmp = function () {
  return { title: 'KMP: failure (LPS) table and search', inputs: [txt('pat', 'Pattern', 'ababaca'), txt('text', 'Text', 'bacbababacabab')],
    build: function (v) {
      const pat = parseStr(v.pat, 10), text = parseStr(v.text, 18), m = pat.length, F = [];
      const lps = new Array(m).fill(0); let k = 0; const p = pat.split('');
      F.push({ msg: 'lps[i] = length of the longest proper prefix of pattern[0..i] that is also a suffix. lps[0] = 0.', rows: [cellsRow('pattern', p, {}, {}), cellsRow('lps', lps, { 0: 'ok' }, {})] });
      for (let i = 1; i < m; i++) {
        while (k > 0 && p[i] !== p[k]) { F.push({ msg: "Mismatch '" + p[i] + "' vs '" + p[k] + "' → fall back: k = lps[" + (k - 1) + "] = " + lps[k - 1] + '.', rows: [cellsRow('pattern', p, { [i]: 'bad', [k]: 'bad' }, { [i]: 'i', [k]: 'k' }), cellsRow('lps', lps, Object.fromEntries(range(0, i - 1).map((x) => [x, 'ok'])), {})] }); k = lps[k - 1]; }
        if (p[i] === p[k]) k++;
        lps[i] = k;
        F.push({ msg: "i = " + i + ": '" + p[i] + "' " + (k > 0 ? 'extends the prefix match → lps[' + i + '] = ' + k + '.' : 'matches no prefix → lps[' + i + '] = 0.'), rows: [cellsRow('pattern', p, { [i]: 'hl' }, { [i]: 'i' }), cellsRow('lps', lps, Object.fromEntries(range(0, i).map((x) => [x, x === i ? 'hl' : 'ok'])), {})] });
      }
      const t = text.split(''); let j = 0; const found = [];
      F.push({ msg: 'LPS table done: [' + lps.join(', ') + ']. Now scan the text; the text pointer never moves backwards.', rows: [cellsRow('text', t, {}, {}), cellsRow('pattern', p, {}, {})] });
      for (let i = 0; i < t.length; i++) {
        while (j > 0 && t[i] !== p[j]) { F.push({ msg: "Mismatch at text[" + i + "]; fall back j = lps[" + (j - 1) + '] = ' + lps[j - 1] + ' (reuse what already matched).', rows: [cellsRow('text', t, { [i]: 'bad' }, { [i]: 'i' }), cellsRow('pattern', p, { [j]: 'bad' }, { [j]: 'j' })] }); j = lps[j - 1]; }
        if (t[i] === p[j]) j++;
        const marks = {}; range(i - j + 1, i).forEach((x) => { marks[x] = 'sel'; });
        if (j === m) { found.push(i - m + 1); range(i - m + 1, i).forEach((x) => { marks[x] = 'ok'; }); F.push({ msg: 'Full match ending at text[' + i + '] → pattern found at index ' + (i - m + 1) + ' ✔', rows: [cellsRow('text', t, marks, { [i]: 'i' }), cellsRow('pattern', p, Object.fromEntries(p.map((_, x) => [x, 'ok'])), {})] }); j = lps[j - 1]; } else F.push({ msg: "text[" + i + "] = '" + t[i] + "' " + (j > 0 ? 'continues the match (' + j + ' chars matched).' : 'matches nothing yet.'), rows: [cellsRow('text', t, marks, { [i]: 'i' }), cellsRow('pattern', p, Object.fromEntries(range(0, Math.max(0, j - 1)).map((x) => [x, j > 0 ? 'sel' : ''])), { [j]: 'j' })] });
      }
      F.push({ msg: found.length ? 'Pattern found at index/indices: ' + found.join(', ') + '. Total work O(n + m).' : 'Pattern not found in the text.', rows: [cellsRow('text', t, Object.fromEntries(found.flatMap((s0) => range(s0, s0 + m - 1)).map((x) => [x, 'ok'])), {})] });
      return F;
    } };
};

VIZ.interval = function () {
  return { title: 'Merge intervals', inputs: [txt('iv', 'Intervals (start-end, …)', '1-3, 2-6, 8-10, 15-18, 9-12')],
    build: function (v) {
      const iv = String(v.iv).split(/[,;]+/).map((x) => x.trim()).filter(Boolean).map((p) => { const m = p.match(/^(\d+)\s*-\s*(\d+)$/); if (!m || +m[1] > +m[2]) throw new Error('Bad interval "' + p + '" - use start-end with start ≤ end.'); return [+m[1], +m[2]]; });
      if (!iv.length || iv.length > 8) throw new Error('Enter 1 to 8 intervals.');
      iv.sort((x, y) => x[0] - y[0]); const F = [], out = [];
      const g = (cur) => ({ label: 'sorted by start (current in yellow)', items: iv.map((x, i) => ({ s: x[0], e: x[1], label: x[0] + '-' + x[1], cls: i === cur ? 'hl' : i < cur ? 'ok' : 'sel' })) });
      const go = (m, cur) => F.push({ msg: m, gantt: g(cur), rows: [kvRow('merged result', out.map((x) => ({ v: '[' + x[0] + ',' + x[1] + ']', cls: 'hl' })))] });
      go('Step 1: sort by start time.', -1);
      iv.forEach((x, i) => {
        if (out.length && x[0] <= out[out.length - 1][1]) { const old = out[out.length - 1][1]; out[out.length - 1][1] = Math.max(old, x[1]); go('[' + x[0] + ',' + x[1] + '] starts at or before the last merged end (' + old + ') → overlap, extend the end to max(' + old + ', ' + x[1] + ') = ' + out[out.length - 1][1] + '.', i); } else { out.push([x[0], x[1]]); go('[' + x[0] + ',' + x[1] + '] does not overlap → start a new merged interval.', i); }
      });
      go('Done: ' + out.length + ' merged interval(s). O(n log n) because of the sort.', iv.length);
      return F;
    } };
};

VIZ.matrix = function () {
  return { title: 'Spiral traversal', inputs: [txt('r', 'Rows (1-6)', '4'), txt('c', 'Columns (1-6)', '5')],
    build: function (v) {
      const R = Math.floor(+v.r), C = Math.floor(+v.c); if (!(R >= 1 && R <= 6 && C >= 1 && C <= 6)) throw new Error('Rows and columns must be between 1 and 6.');
      const ord = range(1, R).map(() => new Array(C).fill(''));
      let top = 0, bot = R - 1, left = 0, right = C - 1, k = 0; const F = [];
      const show = (m, r, c) => F.push({ msg: m, table: { head: range(0, C - 1), corner: '', side: range(0, R - 1), rows: ord.map((row, i) => row.map((x, j) => ({ v: x, cls: i === r && j === c ? 'hl' : x !== '' ? 'ok' : '' }))) }, rows: [kvRow('boundaries', [{ k: 'top', v: top }, { k: 'bottom', v: bot }, { k: 'left', v: left }, { k: 'right', v: right }])] });
      show('Numbers show the visiting order. Four boundaries shrink after each side is walked.');
      const visit = (r, c, m) => { ord[r][c] = ++k; show(m, r, c); };
      while (top <= bot && left <= right) {
        for (let c = left; c <= right; c++) visit(top, c, 'Walk the top row left → right.'); top++;
        for (let r = top; r <= bot; r++) visit(r, right, 'Walk the right column top → bottom.'); right--;
        if (top <= bot) { for (let c = right; c >= left; c--) visit(bot, c, 'Walk the bottom row right → left.'); bot--; }
        if (left <= right) { for (let r = bot; r >= top; r--) visit(r, left, 'Walk the left column bottom → top.'); left++; }
      }
      show('All ' + k + ' cells visited exactly once → O(rows × cols).');
      return F;
    } };
};

/* ---------- greedy ---------- */
VIZ.greedy = function () {
  return { title: 'Greedy vs optimal: coin change', note: 'Try coins 1,3,4 and amount 6', inputs: [txt('coins', 'Coins', '1,3,4'), txt('amt', 'Amount (≤ 60)', '6')],
    build: function (v) {
      const coins = parseNums(v.coins, { max: 6, int: true, min: 1 }), amt = Math.floor(+v.amt); if (!(amt >= 1 && amt <= 60)) throw new Error('Amount must be 1-60.');
      const sorted = coins.slice().sort((a, b) => b - a), F = []; let rem = amt; const taken = [];
      F.push({ msg: 'Greedy rule: always take the largest coin that still fits. Amount = ' + amt + '.', rows: [cellsRow('coins taken', [], {}, {}, true), kvRow('remaining', [{ v: rem }])] });
      for (const c of sorted) while (rem >= c) { rem -= c; taken.push(c); F.push({ msg: 'Take ' + c + ' → remaining ' + rem + '.', rows: [cellsRow('coins taken', taken.slice(), Object.fromEntries(taken.map((_, i) => [i, 'sel'])), {}, true), kvRow('remaining', [{ v: rem }])] }); }
      const greedy = rem === 0 ? taken.length : -1;
      const dp = [0]; const from = [-1]; for (let a = 1; a <= amt; a++) { dp[a] = Infinity; from[a] = -1; coins.forEach((c) => { if (c <= a && dp[a - c] + 1 < dp[a]) { dp[a] = dp[a - c] + 1; from[a] = c; } }); }
      const best = []; if (dp[amt] < Infinity) { let a = amt; while (a > 0) { best.push(from[a]); a -= from[a]; } }
      F.push({ msg: 'Greedy finished: ' + (greedy < 0 ? 'got stuck, leaving ' + rem + ' unmade.' : greedy + ' coin(s) → ' + taken.join(' + ') + '.'), rows: [cellsRow('greedy result', taken, Object.fromEntries(taken.map((_, i) => [i, greedy < 0 ? 'bad' : 'sel'])), {}, true)] });
      F.push({ msg: 'Dynamic programming (tries every combination via dp[a] = min(dp[a−c] + 1)): ' + (dp[amt] === Infinity ? 'impossible.' : dp[amt] + ' coin(s) → ' + best.join(' + ') + '.'), rows: [cellsRow('optimal (DP) result', best, Object.fromEntries(best.map((_, i) => [i, 'ok'])), {}, true)] });
      const diff = greedy !== dp[amt];
      F.push({ msg: diff ? '✘ Greedy is WRONG here: it used ' + (greedy < 0 ? 'no valid answer' : greedy) + ' coin(s) but ' + dp[amt] + ' is possible. Greedy only works for special coin systems (like 1,2,5,10,…).' : '✔ Greedy happened to match the optimum for this input. Try coins 1,3,4 with amount 6 to see it fail.', rows: [cellsRow('greedy', taken, Object.fromEntries(taken.map((_, i) => [i, diff ? 'bad' : 'ok'])), {}, true), cellsRow('optimal', best, Object.fromEntries(best.map((_, i) => [i, 'ok'])), {}, true)] });
      return F;
    } };
};

VIZ.activity = function () {
  return { title: 'Activity selection (sort by finish time)', inputs: [txt('s', 'Start times', '1,3,0,5,8,5'), txt('e', 'End times', '2,4,6,7,9,9')],
    build: function (v) {
      const S = parseNums(v.s, { max: 8 }), E = parseNums(v.e, { max: 8 }); if (S.length !== E.length) throw new Error('Same number of starts and ends needed.'); if (S.some((x, i) => x > E[i])) throw new Error('Each start must be ≤ its end.');
      const acts = S.map((x, i) => [x, E[i]]).sort((a, b) => a[1] - b[1]); const F = []; let last = -Infinity; const st = acts.map(() => 'sel');
      const g = () => ({ label: 'sorted by end time (green = chosen, red = skipped)', items: acts.map((a, i) => ({ s: a[0], e: a[1], label: a[0] + '-' + a[1], cls: st[i] })) });
      F.push({ msg: 'Sort by END time. Take an activity if it starts at or after the end of the last chosen one.', gantt: g() });
      acts.forEach((a, i) => { if (a[0] >= last) { st[i] = 'ok'; last = a[1]; F.push({ msg: a[0] + '-' + a[1] + ' starts at ' + a[0] + ' ≥ last end → CHOOSE it. Last end = ' + last + '.', gantt: g() }); } else { st[i] = 'bad'; F.push({ msg: a[0] + '-' + a[1] + ' starts before the last chosen end → skip (overlap).', gantt: g() }); } });
      F.push({ msg: 'Maximum number of non-overlapping activities = ' + st.filter((x) => x === 'ok').length + '.', gantt: g() });
      return F;
    } };
};

/* ====================== mounting ====================== */
function mountViz(host, key) {
  const parts = key.split(':'); const id = parts[0], param = parts[1];
  if (!VIZ[id]) { host.textContent = 'Visualiser not found: ' + id; return; }
  const spec = VIZ[id](param);
  if (spec.live) spec.live(host); else mountPlayer(host, spec);
}

/* ====================== page integration ====================== */
function mountAll() {
  const slots = Array.prototype.slice.call(document.querySelectorAll('.viz-slot[data-viz]'));
  function mount(el) {
    if (el._mounted) return;
    el._mounted = true;
    try { mountViz(el, el.getAttribute('data-viz')); } catch (e) { el.textContent = 'This visualiser could not load: ' + e.message; }
  }
  if ('IntersectionObserver' in window) {
    const io = new IntersectionObserver(function (entries) {
      entries.forEach(function (en) { if (en.isIntersecting) { io.unobserve(en.target); mount(en.target); } });
    }, { rootMargin: '400px' });
    slots.forEach(function (s) { io.observe(s); });
  } else {
    slots.forEach(mount);
  }
}
if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', mountAll); else mountAll();
})();
