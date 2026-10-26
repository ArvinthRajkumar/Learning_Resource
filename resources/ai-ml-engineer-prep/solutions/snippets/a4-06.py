import random, math
random.seed(2)
d, N, bits = 16, 3000, 10
data = [[random.gauss(0, 1) for _ in range(d)] for _ in range(N)]
planes = [[random.gauss(0, 1) for _ in range(d)] for _ in range(bits)]
sig = lambda v: tuple(sum(a * b for a, b in zip(p, v)) > 0 for p in planes)
buckets = {}
for i, v in enumerate(data):
    buckets.setdefault(sig(v), []).append(i)
q = [x + random.gauss(0, 0.2) for x in data[0]]            # a query close to data[0]
cands = buckets.get(sig(q), [])
best = min(cands, key=lambda i: math.dist(q, data[i])) if cands else None
print("candidates checked:", len(cands), "of", N, "| found the true neighbour:", best == 0)
