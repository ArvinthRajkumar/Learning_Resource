from collections import defaultdict

def build_graph(n, edges, directed=False):
    graph = defaultdict(list)
    for a, b in edges:
        graph[a].append(b)
        if not directed:
            graph[b].append(a)     # undirected: edge both ways
    return graph

def build_matrix(n, edges):
    m = [[0] * n for _ in range(n)]
    for a, b in edges:
        m[a][b] = m[b][a] = 1
    return m
