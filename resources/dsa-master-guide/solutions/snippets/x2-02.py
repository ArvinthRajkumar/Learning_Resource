from collections import deque
def zero_one_bfs(n, adj, src):
    dist = [float("inf")] * n; dist[src] = 0
    dq = deque([src])
    while dq:
        u = dq.popleft()
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                dq.appendleft(v) if w == 0 else dq.append(v)
    return dist
adj = [[(1, 0), (2, 1)], [(3, 1)], [(3, 0)], []]
print(zero_one_bfs(4, adj, 0))
