def origin_load(requests, hit_ratio): return requests * (1 - hit_ratio)
reqs = 10_000_000
for hr in (0.50, 0.90, 0.99):
    print(f"hit ratio {hr:.0%}: origin sees {origin_load(reqs, hr):>9,.0f} of {reqs:,} requests ({(1 - hr):.0%} of traffic)")
print("Raising the hit ratio from 90% to 99% cuts origin traffic by", f"{(1 - 0.99) / (1 - 0.90):.0%} of what it was", "(10x fewer requests).")
