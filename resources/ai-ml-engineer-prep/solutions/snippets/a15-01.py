def pagerank(edges, n, d=0.85, iters=100):
    out = [[] for _ in range(n)]
    for u, v in edges: out[u].append(v)
    pr = [1.0 / n] * n
    for _ in range(iters):
        new = [(1 - d) / n] * n
        for u in range(n):
            if out[u]:
                share = d * pr[u] / len(out[u])
                for v in out[u]: new[v] += share
            else:
                for v in range(n): new[v] += d * pr[u] / n               # dangling node: spread its rank evenly
        pr = new
    return pr
# 0 -> 1, 0 -> 2, 1 -> 2, 2 -> 0, 3 -> 2 ; node 4 links only to 3 ; node 2 is linked to by everybody
edges = [(0, 1), (0, 2), (1, 2), (2, 0), (3, 2), (4, 3)]
pr = pagerank(edges, 5)
for node in sorted(range(5), key=lambda v: -pr[v]): print(f"node {node}: PageRank {pr[node]:.3f}")
print("ranks sum to 1:", round(sum(pr), 6))
