import heapq, random
random.seed(0)
INF = float("inf")

def make_graph(n, m, lo=1, hi=9):
    edges = []
    for _ in range(m):
        u, v = random.randrange(n), random.randrange(n)
        if u != v: edges.append((u, v, random.randint(lo, hi)))
    return edges

def dijkstra(n, edges, src):
    adj = [[] for _ in range(n)]
    for u, v, w in edges: adj[u].append((v, w))
    dist = [INF] * n; dist[src] = 0
    pq = [(0, src)]
    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]: continue                      # stale entry
        for v, w in adj[u]:
            if d + w < dist[v]:
                dist[v] = d + w
                heapq.heappush(pq, (dist[v], v))
    return dist

def bellman_ford(n, edges, src):
    dist = [INF] * n; dist[src] = 0
    for _ in range(n - 1):
        changed = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w; changed = True
        if not changed: break
    for u, v, w in edges:                              # one more pass: any improvement means a negative cycle
        if dist[u] + w < dist[v]: return None
    return dist

n = 30
edges = make_graph(n, 120)
assert dijkstra(n, edges, 0) == bellman_ford(n, edges, 0)
print("Dijkstra equals Bellman-Ford on a random graph with non-negative weights")
neg = [(0, 1, 2), (1, 2, -5), (2, 0, 1)]               # cycle total -2
print("negative cycle detected:", bellman_ford(3, neg, 0) is None)
