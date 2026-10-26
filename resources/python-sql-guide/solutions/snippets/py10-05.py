sales = [("north", "2024-01", 100), ("north", "2024-02", 120), ("north", "2024-03", 90), ("south", "2024-01", 80), ("south", "2024-02", 95), ("south", "2024-03", 130)]
by_region = {}
for region, month, amount in sorted(sales):                                     # sorted by region then month
    by_region.setdefault(region, []).append((month, amount))
for region, series in by_region.items():
    running, prev, out = 0, None, []
    for month, amount in series:
        running += amount
        change = None if prev is None else round(100 * (amount - prev) / prev, 1)
        out.append((month, amount, running, change)); prev = amount
    print(region, out)
ranked = sorted(sales, key=lambda r: -r[2])
print("top 2 overall:", [(r[0], r[1], r[2]) for r in ranked[:2]])
