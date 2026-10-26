from pathlib import Path
import tempfile
p = Path(tempfile.mkdtemp()) / "data" / "a.txt"
p.parent.mkdir(parents=True, exist_ok=True)
p.write_text("hello", encoding="utf-8")
print(p.name, p.suffix, p.stem, p.exists(), p.read_text(encoding="utf-8"))
print([x.name for x in p.parent.glob("*.txt")])
