"""Copy resources.json into the inline fallback block of index.html.

Why: browsers block fetch() on file://, so index.html carries an inline copy.
Run after editing resources.json:  python3 tools/sync_resources.py
"""
import json
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
REQUIRED = {"id", "title", "description", "tags", "path", "updated"}


def main() -> int:
    data = json.loads((ROOT / "resources.json").read_text(encoding="utf-8"))
    for r in data:
        missing = REQUIRED - set(r)
        if missing:
            print(f"{r.get('id', '?')}: missing {sorted(missing)}")
            return 1
        if not (ROOT / r["path"]).exists():
            print(f"{r['id']}: path does not exist: {r['path']}")
            return 1
    index = ROOT / "index.html"
    html = index.read_text(encoding="utf-8")
    block = json.dumps(data, indent=2, ensure_ascii=False)
    new, n = re.subn(
        r"(<!-- resources:start -->\n).*?(\n<!-- resources:end -->)",
        lambda m: m.group(1) + block + m.group(2),
        html,
        flags=re.S,
    )
    if n != 1:
        print("marker block not found in index.html")
        return 1
    index.write_text(new, encoding="utf-8")
    print(f"synced {len(data)} resource(s) into index.html")
    return 0


if __name__ == "__main__":
    sys.exit(main())
