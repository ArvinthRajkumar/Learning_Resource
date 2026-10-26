import random, zlib, json
random.seed(1)
rows = [{"id": i, "country": random.choice(["IN", "US", "DE"]), "amount": random.randint(1, 5) * 10} for i in range(20000)]
row_bytes = zlib.compress(json.dumps(rows).encode(), 6)
cols = {c: [r[c] for r in rows] for c in rows[0]}
col_bytes = sum(len(zlib.compress(json.dumps(v).encode(), 6)) for v in cols.values())
print(f"row layout: {len(row_bytes):,} bytes | column layout: {col_bytes:,} bytes (compressed) | ratio {len(row_bytes) / col_bytes:.2f}x")
