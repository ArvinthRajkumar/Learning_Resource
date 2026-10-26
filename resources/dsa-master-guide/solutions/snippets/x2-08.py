from collections import deque
def is_bipartite(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges: adj[u].append(v); adj[v].append(u)
    color = [-1] * n
    for s in range(n):
        if color[s] != -1: continue
        color[s] = 0; q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if color[v] == -1: color[v] = 1 - color[u]; q.append(v)
                elif color[v] == color[u]: return False
    return True
print("even cycle:", is_bipartite(4, [(0, 1), (1, 2), (2, 3), (3, 0)]), "| triangle:", is_bipartite(3, [(0, 1), (1, 2), (2, 0)]))
