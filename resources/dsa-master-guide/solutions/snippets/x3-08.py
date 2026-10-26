import random, itertools
random.seed(5)
def mis_tree(n, parent):
    kids = [[] for _ in range(n)]
    for v in range(1, n): kids[parent[v]].append(v)
    take, skip = [0] * n, [0] * n
    for v in range(n - 1, -1, -1):                    # parents have smaller index, so this is post-order
        take[v] = 1 + sum(skip[c] for c in kids[v])
        skip[v] = sum(max(take[c], skip[c]) for c in kids[v])
    return max(take[0], skip[0])
def brute(n, parent):
    edges = [(v, parent[v]) for v in range(1, n)]
    best = 0
    for mask in range(1 << n):
        if all(not (mask >> a & 1 and mask >> b & 1) for a, b in edges):
            best = max(best, bin(mask).count("1"))
    return best
for _ in range(60):
    n = random.randint(1, 11)
    parent = [0] + [random.randrange(v) for v in range(1, n)]
    assert mis_tree(n, parent) == brute(n, parent)
print("tree DP (take or skip) verified against subset enumeration")
