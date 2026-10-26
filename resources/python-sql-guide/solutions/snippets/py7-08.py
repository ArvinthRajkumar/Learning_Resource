import gzip, zipfile, io, json
payload = json.dumps([{"id": i, "text": "repeat " * 20} for i in range(200)]).encode()
gz = gzip.compress(payload)
print(f"gzip: {len(payload):,} -> {len(gz):,} bytes ({len(gz) / len(payload):.1%}) | round trip ok: {gzip.decompress(gz) == payload}")
buf = io.BytesIO()
with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as z:
    z.writestr("a.txt", "hello " * 50); z.writestr("dir/b.txt", "world")
with zipfile.ZipFile(io.BytesIO(buf.getvalue())) as z:
    print("zip members:", z.namelist(), "| read b:", z.read("dir/b.txt").decode())
