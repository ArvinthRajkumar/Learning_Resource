from collections import deque
def max_flow(n, cap, s, t):
    flow = 0
    while True:
        parent = [-1] * n; parent[s] = s
        q = deque([s])
        while q and parent[t] == -1:
            u = q.popleft()
            for v in range(n):
                if parent[v] == -1 and cap[u][v] > 0:
                    parent[v] = u; q.append(v)
        if parent[t] == -1: return flow
        bottleneck, v = float("inf"), t
        while v != s:
            bottleneck = min(bottleneck, cap[parent[v]][v]); v = parent[v]
        v = t
        while v != s:
            cap[parent[v]][v] -= bottleneck; cap[v][parent[v]] += bottleneck; v = parent[v]
        flow += bottleneck
cap = [[0, 10, 10, 0, 0, 0],
       [0, 0, 2, 4, 8, 0],
       [0, 0, 0, 0, 9, 0],
       [0, 0, 0, 0, 0, 10],
       [0, 0, 0, 6, 0, 10],
       [0, 0, 0, 0, 0, 0]]
print("maximum flow:", max_flow(6, cap, 0, 5))
