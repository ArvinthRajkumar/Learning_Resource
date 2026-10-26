import random
random.seed(1)
def random_tree(n):
    return [(random.randrange(i), i) for i in range(1, n)]            # edge (parent, child); node 0 is the root
def build(n, edges):
    adj = [[] for _ in range(n)]
    for a, b in edges: adj[a].append(b); adj[b].append(a)
    return adj
def dfs_info(n, adj, root=0):
    parent, depth, order, size = [-1] * n, [0] * n, [], [1] * n
    stack = [root]
    while stack:                                                       # iterative preorder
        u = stack.pop(); order.append(u)
        for v in adj[u]:
            if v != parent[u]: parent[v], depth[v] = u, depth[u] + 1; stack.append(v)
    for u in reversed(order):                                          # children before parents
        if parent[u] >= 0: size[parent[u]] += size[u]
    return parent, depth, order, size
n = 12; edges = random_tree(n); adj = build(n, edges)
parent, depth, order, size = dfs_info(n, adj)
print("parent:", parent); print("depth :", depth); print("subtree sizes:", size, "| root size is n:", size[0] == n)
