INF = float("inf")
def floyd(n, edges):
    d = [[0 if i == j else INF for j in range(n)] for i in range(n)]
    for u, v, w in edges: d[u][v] = min(d[u][v], w)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if d[i][k] + d[k][j] < d[i][j]:
                    d[i][j] = d[i][k] + d[k][j]
    return d
edges = [(0, 1, 3), (1, 2, -2), (0, 2, 4), (2, 3, 2), (3, 0, 7)]
for row in floyd(4, edges): print(row)
