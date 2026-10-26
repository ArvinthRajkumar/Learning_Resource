import sys
sys.setrecursionlimit(10000)
def bridges(n, edges):
    adj = [[] for _ in range(n)]
    for i, (u, v) in enumerate(edges):
        adj[u].append((v, i)); adj[v].append((u, i))
    tin, low, timer, out = [-1] * n, [0] * n, [0], []
    def dfs(u, parent_edge):
        tin[u] = low[u] = timer[0]; timer[0] += 1
        for v, i in adj[u]:
            if i == parent_edge: continue
            if tin[v] != -1:
                low[u] = min(low[u], tin[v])
            else:
                dfs(v, i)
                low[u] = min(low[u], low[v])
                if low[v] > tin[u]: out.append(edges[i])
    for u in range(n):
        if tin[u] == -1: dfs(u, -1)
    return out
edges = [(0, 1), (1, 2), (2, 0), (1, 3), (3, 4), (4, 5), (5, 3), (5, 6)]
print("bridges:", bridges(7, edges))
