import bisect, hashlib
h = lambda s: int(hashlib.md5(s.encode()).hexdigest(), 16)
def build_ring(nodes, vnodes=100): return sorted((h(f"{n}#{v}"), n) for n in nodes for v in range(vnodes))
def owner(ring, key):
    hashes = [x[0] for x in ring]
    return ring[bisect.bisect(hashes, h(key)) % len(ring)][1]
keys = [f"user{i}" for i in range(10_000)]
r4, r5 = build_ring(["A", "B", "C", "D"]), build_ring(["A", "B", "C", "D", "E"])
moved = sum(owner(r4, k) != owner(r5, k) for k in keys)
print(f"consistent hashing: adding a 5th node moves {moved / len(keys):.0%} of keys (ideal is 20%)")
