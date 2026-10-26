from collections import deque
graph = {"A": ["B", "C"], "B": ["D"], "C": ["D", "E"], "D": ["F"], "E": ["F"], "F": []}
def bfs_levels(start):
    seen, q, out = {start}, deque([start]), []
    while q:
        u = q.popleft(); out.append(u)
        for v in graph[u]:
            if v not in seen: seen.add(v); q.append(v)
    return out
def dfs_order(u, seen=None):
    seen = seen if seen is not None else set(); seen.add(u); out = [u]
    for v in graph[u]:
        if v not in seen: out += dfs_order(v, seen)
    return out
print("BFS (ring by ring):", bfs_levels("A"), "| DFS (deep first):", dfs_order("A"))
