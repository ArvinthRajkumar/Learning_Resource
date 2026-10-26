rows = [{"order": 1, "country": "IN", "amount": 120.0}, {"order": 2, "country": "US", "amount": 80.5}, {"order": 3, "country": "IN", "amount": 45.0}, {"order": 4, "country": "DE", "amount": None}]
big = [r for r in rows if r["amount"] is not None and r["amount"] > 50]                   # filter (WHERE)
projected = [{k: r[k] for k in ("order", "amount")} for r in rows]                          # select columns
with_tax = [{**r, "gross": round(r["amount"] * 1.18, 2) if r["amount"] is not None else None} for r in rows]   # new column
print([r["order"] for r in big]); print(projected[0]); print([r["gross"] for r in with_tax])
