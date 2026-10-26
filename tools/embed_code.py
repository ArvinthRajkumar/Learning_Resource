"""Embed source files into HTML pages so the page shows exactly the tested code.

In a page:  <pre><code class="lang-py" data-embed="solutions/bm25.py"></code></pre>
The path is relative to the HTML file. Running this script replaces the
content of every such <code> element with the HTML-escaped file text.
It is idempotent: run it after editing any solution file.

Usage:  python3 tools/embed_code.py [html files...]   (default: every .html under resources/)
"""
import html
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PATTERN = re.compile(r'(<code\b[^>]*\bdata-embed="([^"]+)"[^>]*>)(.*?)(</code>)', re.S)


def embed(page: pathlib.Path) -> int:
    text = page.read_text(encoding="utf-8")
    count = 0

    def repl(m):
        nonlocal count
        src = (page.parent / m.group(2)).resolve()
        if not src.exists():
            raise SystemExit(f"{page}: missing embed source {m.group(2)}")
        count += 1
        return m.group(1) + html.escape(src.read_text(encoding="utf-8").rstrip("\n"), quote=False) + m.group(4)

    new = PATTERN.sub(repl, text)
    if new != text:
        page.write_text(new, encoding="utf-8")
    return count


def main() -> int:
    pages = [pathlib.Path(p).resolve() for p in sys.argv[1:]] or sorted((ROOT / "resources").rglob("*.html"))
    total = 0
    for p in pages:
        n = embed(p)
        if n:
            print(f"{p.relative_to(ROOT)}: {n} block(s)")
        total += n
    print(f"embedded {total} code block(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
