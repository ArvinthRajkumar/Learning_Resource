def count_components(n, edges):
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    seen = set()
    def dfs(u):
        seen.add(u)
        for v in graph[u]:
            if v not in seen:
                dfs(v)
    comps = 0
    for i in range(n):
        if i not in seen:
            comps += 1
            dfs(i)
    return comps
