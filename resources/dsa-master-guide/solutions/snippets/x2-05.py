import heapq, random
random.seed(1)
class DSU:
    def __init__(self, n): self.p, self.sz = list(range(n)), [1] * n
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x
    def union(self, a, b):
        a, b = self.find(a), self.find(b)
        if a == b: return False
        if self.sz[a] < self.sz[b]: a, b = b, a
        self.p[b] = a; self.sz[a] += self.sz[b]
        return True
def kruskal(n, edges):
    d, total = DSU(n), 0
    for u, v, w in sorted(edges, key=lambda e: e[2]):
        if d.union(u, v): total += w
    return total
def prim(n, edges):
    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u].append((w, v)); adj[v].append((w, u))
    seen, total, pq = set(), 0, [(0, 0)]
    while pq and len(seen) < n:
        w, u = heapq.heappop(pq)
        if u in seen: continue
        seen.add(u); total += w
        for e in adj[u]:
            if e[1] not in seen: heapq.heappush(pq, e)
    return total
n = 25
edges = [(i, i + 1, random.randint(1, 20)) for i in range(n - 1)]                  # a path guarantees connectivity
edges += [(random.randrange(n), random.randrange(n), random.randint(1, 20)) for _ in range(60)]
edges = [e for e in edges if e[0] != e[1]]
assert kruskal(n, edges) == prim(n, edges)
print("Kruskal and Prim agree: MST weight", kruskal(n, edges))
