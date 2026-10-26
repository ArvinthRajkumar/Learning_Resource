import gzip, json, zlib
rows = [{"id": i, "name": f"product {i % 50}", "category": ["tools", "toys", "books"][i % 3], "price": 10 + i % 7} for i in range(2000)]
raw = json.dumps(rows).encode()
print(f"JSON {len(raw):,} bytes -> gzip {len(gzip.compress(raw)):,} bytes ({len(gzip.compress(raw)) / len(raw):.1%}) -> zlib level 9 {len(zlib.compress(raw, 9)):,}")
slim = json.dumps([[r["id"], r["name"], r["category"], r["price"]] for r in rows], separators=(",", ":")).encode()
print(f"array-of-arrays {len(slim):,} bytes -> gzip {len(gzip.compress(slim)):,} bytes (compression already removes most key repetition)")
