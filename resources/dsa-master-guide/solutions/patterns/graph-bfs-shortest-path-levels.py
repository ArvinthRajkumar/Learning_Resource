from collections import deque

def bfs_dist(graph, start):
    dist, q = {start: 0}, deque([start])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if v not in dist:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist
