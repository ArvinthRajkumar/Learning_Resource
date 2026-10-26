from collections import deque

def can_finish(n, prereqs):
    graph = [[] for _ in range(n)]
    indeg = [0] * n
    for a, b in prereqs:
        graph[b].append(a)
        indeg[a] += 1
    q = deque(i for i in range(n) if indeg[i] == 0)
    done = 0
    while q:
        node = q.popleft()
        done += 1
        for nb in graph[node]:
            indeg[nb] -= 1
            if indeg[nb] == 0:
                q.append(nb)
    return done == n
