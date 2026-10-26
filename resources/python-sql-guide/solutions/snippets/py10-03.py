from collections import defaultdict
from statistics import mean
rows = [("IN", 120.0), ("US", 80.5), ("IN", 45.0), ("DE", None), ("US", 200.0), ("IN", 30.0)]
groups = defaultdict(list)
for country, amount in rows:
    if amount is not None: groups[country].append(amount)                      # skip missing, as SQL aggregates do
summary = {c: {"n": len(v), "total": sum(v), "mean": round(mean(v), 2), "max": max(v)} for c, v in groups.items()}
for c in sorted(summary, key=lambda c: -summary[c]["total"]): print(c, summary[c])
print("groups with no valid amount are absent:", "DE" not in summary)
