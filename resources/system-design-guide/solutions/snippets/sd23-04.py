import math, random
random.seed(0)
d, N = 16, 2000
vecs = [[random.gauss(0, 1) for _ in range(d)] for _ in range(N)]
norm = lambda v: math.sqrt(sum(x * x for x in v))
unit = lambda v: [x / norm(v) for x in v]
db = [unit(v) for v in vecs]
q = unit([x + random.gauss(0, 0.3) for x in vecs[123]])          # a noisy copy of item 123
dot = lambda a, b: sum(x * y for x, y in zip(a, b))
best = sorted(range(N), key=lambda i: -dot(db[i], q))[:3]
print("exact top-3 by cosine similarity:", best, "(item 123 should be first)")
# IVF-style: assign to 20 random centroids, search only the nearest 3 clusters
cents = random.sample(db, 20)
assign = [max(range(20), key=lambda c: dot(db[i], cents[c])) for i in range(N)]
near = sorted(range(20), key=lambda c: -dot(q, cents[c]))[:3]
cand = [i for i in range(N) if assign[i] in near]
approx = sorted(cand, key=lambda i: -dot(db[i], q))[:3]
print(f"approximate search scanned {len(cand)} of {N} vectors, top-3:", approx, "| finds item 123:", 123 in approx)
