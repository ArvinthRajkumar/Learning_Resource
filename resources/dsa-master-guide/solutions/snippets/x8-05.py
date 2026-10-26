import random
from collections import deque
random.seed(5)
def sum_distances_all_roots(n, adj):
    parent, order = [-1] * n, []
    stack = [0]
    while stack:
        u = stack.pop(); order.append(u)
        for v in adj[u]:
            if v != parent[u]: parent[v] = u; stack.append(v)
    size, down = [1] * n, [0] * n
    for u in reversed(order):                                           # down pass
        p = parent[u]
        if p >= 0: size[p] += size[u]; down[p] += down[u] + size[u]
    ans = [0] * n; ans[0] = down[0]
    for u in order[1:]:                                                 # up pass: parents are processed first
        ans[u] = ans[parent[u]] - size[u] + (n - size[u])
    return ans
def brute(n, adj):
    out = []
    for s in range(n):
        dist = {s: 0}; q = deque([s])
        while q:
            u = q.popleft()
            for v in adj[u]:
                if v not in dist: dist[v] = dist[u] + 1; q.append(v)
        out.append(sum(dist.values()))
    return out
for _ in range(200):
    n = random.randint(1, 15)
    adj = [[] for _ in range(n)]
    for i in range(1, n):
        p = random.randrange(i); adj[p].append(i); adj[i].append(p)
    assert sum_distances_all_roots(n, adj) == brute(n, adj)
print("rerooting matches brute force on 200 random trees; star with 4 leaves:", sum_distances_all_roots(5, [[1, 2, 3, 4], [0], [0], [0], [0]]))
