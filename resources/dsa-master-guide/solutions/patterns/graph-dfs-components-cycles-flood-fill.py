def count_components(n, edges):
    g = [[] for _ in range(n)]
    for a, b in edges:
        g[a].append(b); g[b].append(a)
    seen = set()
    def dfs(u):
        seen.add(u)
        for v in g[u]:
            if v not in seen:
                dfs(v)
    comps = 0
    for i in range(n):
        if i not in seen:
            comps += 1
            dfs(i)
    return comps
