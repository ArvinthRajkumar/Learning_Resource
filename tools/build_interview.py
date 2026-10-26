"""Render the interview question bank into pages.

Source of truth: resources/<id>/data/interview-questions.json
  {"questions": [{"topic": "...", "level": "basic|medium|advanced", "q": "...", "a": "...", "kind": "optional tag"}]}
  A question or answer may contain ``` fenced code, which is rendered as a code block.

Targets (in any page under resources/):
  <div class="iq-list" data-iq="Topic"></div><!-- /iq -->       questions of one topic
  <div class="iq-bank"></div><!-- /iqbank -->                    every topic, one tracked section each
Idempotent: run after editing the JSON.
Usage:  python3 tools/build_interview.py
"""
import html
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LEVELS = [("basic", "ok", "Basic"), ("medium", "warn", "Medium"), ("advanced", "bad", "Advanced")]
RANK = {k: i for i, (k, _, _) in enumerate(LEVELS)}
TAG = {k: (c, label) for k, c, label in LEVELS}
LIST_RE = re.compile(r'(<div class="iq-list" data-iq="([^"]+)">)(.*?)(</div><!-- /iq -->)', re.S)
BANK_RE = re.compile(r'(<div class="iq-bank">)(.*?)(</div><!-- /iqbank -->)', re.S)


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def rich(text):
    """Plain paragraphs, with ``` fences rendered as code blocks."""
    out = []
    for i, part in enumerate(text.split("```")):
        if i % 2:
            out.append('<pre><code class="lang-py">%s</code></pre>' % html.escape(part.strip("\n"), quote=False))
        elif part.strip():
            out.append("<p>%s</p>" % html.escape(part.strip()))
    return "".join(out)


def item(q):
    cls, label = TAG[q["level"]]
    kind = q.get("kind")
    kind_tag = f'<span class="tag">{html.escape(kind)}</span> ' if kind else ""
    head, _, code = q["q"].partition("```")
    code_block = rich("```" + code) if code else ""
    return (f'<details class="recall iq" data-level="{q["level"]}" data-topic="{html.escape(q["topic"])}">'
            f'<summary><span class="tag {cls}">{label}</span> {kind_tag}{html.escape(head.strip())}</summary>'
            f'<div class="answer">{code_block}{rich(q["a"])}</div></details>')


def render_list(qs):
    qs = sorted(qs, key=lambda q: RANK[q["level"]])
    return "\n" + "\n".join(item(q) for q in qs) + "\n"


def render_bank(qs):
    topics = []
    for q in qs:
        if q["topic"] not in topics:
            topics.append(q["topic"])
    out = ["\n"]
    for t in topics:
        group = [q for q in qs if q["topic"] == t]
        out.append(f'<section id="iq-{slug(t)}" class="iq-group" data-track data-topic="{html.escape(t)}">\n'
                   f'<h2>{html.escape(t)} <span class="muted small">({len(group)})</span></h2>'
                   + render_list(group) + "</section>\n")
    return "".join(out)


def main() -> int:
    total = 0
    for data in ROOT.glob("resources/*/data/interview-questions.json"):
        qs = json.loads(data.read_text(encoding="utf-8"))["questions"]
        for q in qs:
            if q["level"] not in RANK or not q["q"] or not q["a"]:
                raise SystemExit(f"bad question entry: {q}")
        topics = {q["topic"] for q in qs}
        res_dir = data.parent.parent
        for page in sorted(res_dir.glob("*.html")):
            text = page.read_text(encoding="utf-8")

            def list_repl(m):
                nonlocal total
                topic = m.group(2)
                if topic not in topics:
                    raise SystemExit(f"{page.name}: unknown interview topic {topic!r}")
                group = [q for q in qs if q["topic"] == topic]
                total += len(group)
                return m.group(1) + render_list(group) + m.group(4)

            new = LIST_RE.sub(list_repl, text)
            new = BANK_RE.sub(lambda m: m.group(1) + render_bank(qs) + m.group(3), new)
            if new != text:
                page.write_text(new, encoding="utf-8")
                print(f"updated {page.relative_to(ROOT)}")
        print(f"{data.relative_to(ROOT)}: {len(qs)} questions, {len(topics)} topics")
    print(f"rendered {total} topic-page questions")
    return 0


if __name__ == "__main__":
    sys.exit(main())
