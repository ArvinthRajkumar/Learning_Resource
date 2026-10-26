import random
random.seed(2)
LOG = 5
def preprocess(n, parent):
    up = [[0] * n for _ in range(LOG)]
    for v in range(n): up[0][v] = parent[v] if parent[v] >= 0 else v          # the root is its own ancestor
    for k in range(1, LOG):
        for v in range(n): up[k][v] = up[k - 1][up[k - 1][v]]
    return up
def lca(u, v, depth, up):
    if depth[u] < depth[v]: u, v = v, u
    diff = depth[u] - depth[v]
    for k in range(LOG):
        if diff >> k & 1: u = up[k][u]
    if u == v: return u
    for k in reversed(range(LOG)):
        if up[k][u] != up[k][v]: u, v = up[k][u], up[k][v]
    return up[0][u]
def lca_naive(u, v, parent, depth):
    while depth[u] > depth[v]: u = parent[u]
    while depth[v] > depth[u]: v = parent[v]
    while u != v: u, v = parent[u], parent[v]
    return u
def kth_ancestor(v, k, up):
    for i in range(LOG):
        if k >> i & 1: v = up[i][v]
    return v
n = 30
parent = [-1] + [random.randrange(i) for i in range(1, n)]
depth = [0] * n
for v in range(1, n): depth[v] = depth[parent[v]] + 1
up = preprocess(n, parent)
for _ in range(500):
    u, v = random.randrange(n), random.randrange(n)
    assert lca(u, v, depth, up) == lca_naive(u, v, parent, depth)
print("binary lifting LCA matches the naive walk on 500 random queries")
deep = max(range(n), key=lambda v: depth[v])
print("deepest node", deep, "at depth", depth[deep], "| its 2nd ancestor:", kth_ancestor(deep, 2, up), "equals walking up twice:", parent[parent[deep]] if depth[deep] >= 2 else None)
