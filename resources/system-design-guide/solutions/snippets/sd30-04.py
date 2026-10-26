import math
def servers_needed(peak_qps, qps_per_server, headroom=0.6, failure_domains=3, tolerate_lost=1):
    usable = qps_per_server * headroom
    base = math.ceil(peak_qps / usable)
    survive = math.ceil(peak_qps / (usable)) + math.ceil(base / failure_domains) * tolerate_lost   # N + one zone's worth
    return base, survive
base, safe = servers_needed(peak_qps=30_000, qps_per_server=1_500)
print(f"30k QPS peak, 1.5k QPS per server at 60% target utilisation: {base} servers; {safe} to survive losing one of 3 zones")
print("Little's law: in-flight requests =", 2000 * 0.050)
