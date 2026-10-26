import tempfile
from pathlib import Path
root = Path(tempfile.mkdtemp())
(root / "data").mkdir()
f = root / "data" / "notes.txt"
f.write_text("line one\nline two\nline three\n", encoding="utf8")
print("name:", f.name, "| stem:", f.stem, "| suffix:", f.suffix, "| parent:", f.parent.name)
print("exists:", f.exists(), "| is_file:", f.is_file(), "| non-empty:", f.stat().st_size > 0)
print("lines:", f.read_text(encoding="utf8").splitlines())
(root / "data" / "b.csv").write_text("x\n1\n"); (root / "data" / "a.csv").write_text("x\n2\n")
print("csv files:", sorted(p.name for p in (root / "data").glob("*.csv")))
print("recursive:", sorted(str(p.relative_to(root)).replace("\\", "/") for p in root.rglob("*") if p.is_file()))
print("with_suffix:", f.with_suffix(".md").name)
