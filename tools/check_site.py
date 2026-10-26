"""Static checks for the whole site. Python 3 standard library only.

Checks:
  - HTML structure: void elements aside, every opened tag is closed in order
  - local links and src attributes resolve, and #fragments exist in the target page
  - no external requests (http/https in src, or stylesheet links to other hosts)
  - no duplicate ids per page
  - every .quiz has data-type and data-answer; option answers exist as data-key
  - quiz data-qid values are unique across the site
  - section[data-track] counts match "sections" in each resource's parts.js
  - no em dash (U+2014) or en dash (U+2013) in any text file
Usage:  python3 tools/check_site.py
"""
import json
import pathlib
import re
import sys
from html.parser import HTMLParser
from urllib.parse import urlparse

ROOT = pathlib.Path(__file__).resolve().parent.parent
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr",
        "path", "circle", "rect", "line", "polyline", "polygon", "ellipse", "stop", "use"}
TEXT_EXT = {".html", ".css", ".js", ".py", ".md", ".json"}


class Page(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack, self.errors, self.ids, self.links = [], [], [], []
        self.quizzes, self.sections = [], 0
        self._quiz = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if "id" in a:
            self.ids.append(a["id"])
        for key in ("href", "src"):
            if key in a:
                self.links.append((tag, key, a[key], a.get("rel")))
        cls = a.get("class", "") or ""
        if tag == "section" and "data-track" in a:
            self.sections += 1
        if "quiz" in cls.split() and tag == "div":
            self._quiz = {"qid": a.get("data-qid"), "type": a.get("data-type"), "answer": a.get("data-answer"),
                          "keys": [], "inputs": 0, "line": self.getpos()[0]}
            self.quizzes.append(self._quiz)
        if self._quiz is not None:
            if tag == "li" and "data-key" in a:
                self._quiz["keys"].append(a["data-key"])
            if tag == "input" and "q-input" in cls:
                self._quiz["inputs"] += 1
        if tag not in VOID:
            self.stack.append((tag, self.getpos()[0]))

    def handle_startendtag(self, tag, attrs):
        # self-closing form (<rect ... />): register attributes without pushing
        if tag in VOID:
            self.handle_starttag(tag, attrs)
        else:
            self.handle_starttag(tag, attrs)
            self.stack.pop()

    def handle_endtag(self, tag):
        if tag in VOID:
            return
        if not self.stack:
            self.errors.append(f"line {self.getpos()[0]}: stray </{tag}>")
            return
        top, line = self.stack.pop()
        if top != tag:
            self.errors.append(f"line {self.getpos()[0]}: </{tag}> closes <{top}> from line {line}")
            self.stack.append((top, line))
            # try to recover: pop until match
            for i in range(len(self.stack) - 1, -1, -1):
                if self.stack[i][0] == tag:
                    del self.stack[i:]
                    break
        if tag == "div" and self._quiz is not None and not any(t == "div" for t, _ in self.stack[-50:]):
            pass


def parse(path):
    p = Page()
    p.feed(path.read_text(encoding="utf-8"))
    p.close()
    if p.stack:
        p.errors.append("unclosed: " + ", ".join(f"<{t}> line {l}" for t, l in p.stack[-5:]))
    return p


def main() -> int:
    problems = []
    pages = sorted(ROOT.rglob("*.html"))
    parsed = {pg: parse(pg) for pg in pages}
    all_qids = {}
    for pg, p in parsed.items():
        rel = pg.relative_to(ROOT)
        problems += [f"{rel}: {e}" for e in p.errors]
        dup = {i for i in p.ids if p.ids.count(i) > 1}
        if dup:
            problems.append(f"{rel}: duplicate ids {sorted(dup)}")
        for tag, key, url, rel_attr in p.links:
            u = urlparse(url)
            if u.scheme in ("http", "https"):
                if key == "src" or (tag == "link" and rel_attr == "stylesheet"):
                    problems.append(f"{rel}: external resource {url}")
                continue
            if u.scheme in ("mailto", "javascript", "data"):
                continue
            if pg.parent.name == "templates" and not u.path.startswith("#"):
                continue  # template paths are written for resources/<id>/ depth
            target = (pg.parent / u.path).resolve() if u.path else pg
            if not target.exists():
                problems.append(f"{rel}: broken link {url}")
                continue
            if u.fragment and target.suffix == ".html":
                tids = parsed[target].ids if target in parsed else []
                if u.fragment not in tids:
                    problems.append(f"{rel}: missing anchor {url}")
        for q in p.quizzes:
            where = f"{rel}:{q['line']}"
            if not q["type"] or q["answer"] is None:
                problems.append(f"{where}: quiz missing data-type/data-answer")
                continue
            if q["qid"]:
                if q["qid"] in all_qids:
                    problems.append(f"{where}: duplicate data-qid {q['qid']} (also {all_qids[q['qid']]})")
                all_qids[q["qid"]] = where
            if q["type"] in ("single", "multi"):
                ans = [a.strip() for a in q["answer"].split(",")]
                if any(a not in q["keys"] for a in ans):
                    problems.append(f"{where}: answer {ans} not among options {q['keys']}")
                if q["type"] == "single" and len(ans) != 1:
                    problems.append(f"{where}: single-choice quiz with {len(ans)} answers")
            if q["type"] == "fill" and q["inputs"] and q["inputs"] != len(q["answer"].split("||")):
                problems.append(f"{where}: {q['inputs']} blanks but {len(q['answer'].split('||'))} answer groups")
            if q["type"] == "numeric":
                try:
                    float(q["answer"])
                except ValueError:
                    problems.append(f"{where}: numeric answer not a number")

    # parts.js section counts
    for parts in ROOT.glob("resources/*/parts.js"):
        src = parts.read_text(encoding="utf-8")
        for file, n in re.findall(r'file:\s*"([^"]+)"[^}]*sections:\s*(\d+)', src):
            pg = parts.parent / file
            if not pg.exists():
                problems.append(f"{parts.relative_to(ROOT)}: missing page {file}")
            elif parsed[pg].sections != int(n):
                problems.append(f"{parts.relative_to(ROOT)}: {file} has {parsed[pg].sections} tracked sections, manifest says {n}")

    # resources.json paths
    for r in json.loads((ROOT / "resources.json").read_text(encoding="utf-8")):
        if not (ROOT / r["path"]).exists():
            problems.append(f"resources.json: missing {r['path']}")

    # dashes
    for f in ROOT.rglob("*"):
        if f.is_file() and f.suffix in TEXT_EXT and ".git" not in f.parts:
            for n, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
                if chr(0x2014) in line or chr(0x2013) in line:
                    problems.append(f"{f.relative_to(ROOT)}:{n}: em/en dash")

    print(f"checked {len(pages)} pages, {sum(len(p.quizzes) for p in parsed.values())} quizzes, "
          f"{sum(len(p.links) for p in parsed.values())} links")
    for pr in problems:
        print("  PROBLEM", pr)
    print("OK" if not problems else f"{len(problems)} problem(s)")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
