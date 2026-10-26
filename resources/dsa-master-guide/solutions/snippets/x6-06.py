import random, itertools
random.seed(4)
def vc_two_approx(edges):
    cover, used = set(), set()
    for u, v in edges:
        if u not in used and v not in used:
            cover |= {u, v}; used |= {u, v}
    return cover
def vc_opt(n, edges):
    for k in range(n + 1):
        for c in itertools.combinations(range(n), k):
            s = set(c)
            if all(u in s or v in s for u, v in edges): return k
worst = 0
for _ in range(200):
    n = 8
    edges = [(i, j) for i in range(n) for j in range(i + 1, n) if random.random() < 0.3]
    if not edges: continue
    approx = len(vc_two_approx(edges)); opt = vc_opt(n, edges)
    assert approx <= 2 * opt
    worst = max(worst, approx / opt)
print("2-approximation never exceeded factor 2; worst observed ratio:", round(worst, 2))
