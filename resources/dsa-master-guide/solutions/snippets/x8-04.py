import random, itertools
from collections import deque
random.seed(4)
def bfs(adj, src):
    dist = {src: 0}; q = deque([src])
    while q:
        u = q.popleft()
        for v in adj[u]:
            if v not in dist: dist[v] = dist[u] + 1; q.append(v)
    return dist
def diameter(adj):
    d0 = bfs(adj, 0); a = max(d0, key=d0.get)
    da = bfs(adj, a); b = max(da, key=da.get)
    return da[b], a, b
for _ in range(200):
    n = random.randint(2, 12)
    adj = [[] for _ in range(n)]
    for i in range(1, n):
        p = random.randrange(i); adj[p].append(i); adj[i].append(p)
    best = max(bfs(adj, s)[t] for s in range(n) for t in range(n))
    assert diameter(adj)[0] == best
print("two-pass diameter matches the brute-force maximum over all pairs on 200 random trees")
path_adj = [[1], [0, 2], [1, 3], [2, 4], [3]]
print("diameter of a path of 5 nodes:", diameter(path_adj)[0])
