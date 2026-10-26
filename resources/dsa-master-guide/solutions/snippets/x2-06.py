import sys
sys.setrecursionlimit(10000)
def scc(n, edges):
    adj = [[] for _ in range(n)]; radj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v); radj[v].append(u)
    seen, order = [False] * n, []
    def dfs1(u):
        seen[u] = True
        for v in adj[u]:
            if not seen[v]: dfs1(v)
        order.append(u)
    for u in range(n):
        if not seen[u]: dfs1(u)
    comp = [-1] * n
    def dfs2(u, c):
        comp[u] = c
        for v in radj[u]:
            if comp[v] < 0: dfs2(v, c)
    c = 0
    for u in reversed(order):
        if comp[u] < 0:
            dfs2(u, c); c += 1
    return comp, c
edges = [(0, 1), (1, 2), (2, 0), (2, 3), (3, 4), (4, 5), (5, 3), (6, 5)]
comp, k = scc(7, edges)
print("components:", k, "labels:", comp)
