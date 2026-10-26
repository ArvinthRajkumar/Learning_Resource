"""Re-run every Python and SQL example shown in this resource and compare with the recorded output.

Usage:  python3 resources/<this-resource>/solutions/test_snippets.py
Python snippets run in a subprocess and must print exactly the recorded text.
SQL snippets run in an in-memory SQLite database built from datasets/<name>.sql.
"""
import json
import pathlib
import sqlite3
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent


def statements(code):
    out, cur = [], ""
    for line in code.splitlines(True):
        cur += line
        if sqlite3.complete_statement(cur):
            out.append(cur.strip())
            cur = ""
    if cur.strip():
        out.append(cur.strip())
    return out


def cell(v):
    if v is None:
        return "NULL"
    if isinstance(v, float):
        return repr(round(v, 6)) if v != int(v) else repr(v)
    return str(v)


def main():
    manifest = json.loads((HERE / "snippets.json").read_text(encoding="utf8"))
    failed = 0
    for name, info in sorted(manifest.items()):
        f = HERE / "snippets" / name
        code = f.read_text(encoding="utf8")
        want = f.with_suffix(".out").read_text(encoding="utf8")
        if info["kind"] == "py":
            r = subprocess.run([sys.executable, "-I", "-X", "utf8", str(f)], capture_output=True, text=True, stdin=subprocess.DEVNULL, timeout=60)
            got = r.stdout
            ok = r.returncode == 0 and got == want
        else:
            con = sqlite3.connect(":memory:", isolation_level=None)
            con.executescript((HERE / "datasets" / (info["ds"] + ".sql")).read_text(encoding="utf8"))
            chunks = []
            for st in statements(code):
                if all(l.strip().startswith("--") or not l.strip() for l in st.splitlines()):
                    continue
                try:
                    cur = con.execute(st)
                except sqlite3.Error as e:
                    if not info.get("err"):
                        raise
                    chunks.append("error\n" + str(e))
                    break
                if cur.description:
                    names, data = [d[0] for d in cur.description], cur.fetchall()
                    if st.lstrip().upper().startswith("EXPLAIN QUERY PLAN"):
                        names = ["plan"]
                        data = [[str(r[-1]).replace("SCAN TABLE ", "SCAN ").replace("SEARCH TABLE ", "SEARCH ")] for r in data]
                    rows = [" | ".join(names)] + [" | ".join(cell(v) for v in r) for r in data]
                    chunks.append("\n".join(rows))
            got = "\n\n".join(chunks).rstrip() + "\n"
            ok = got == want
            con.close()
        if not ok:
            failed += 1
            print("FAIL", name)
            print("--- want\n" + want + "--- got\n" + got)
    print("checked %d snippets, %d failed" % (len(manifest), failed))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
