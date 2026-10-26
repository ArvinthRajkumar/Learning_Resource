import random
random.seed(8)
class Node:
    def __init__(self, v): self.v, self.l, self.r = v, None, None
def build(vals):
    nodes = [Node(v) for v in vals]
    for i, n in enumerate(nodes):
        if 2 * i + 1 < len(nodes): n.l = nodes[2 * i + 1]
        if 2 * i + 2 < len(nodes): n.r = nodes[2 * i + 2]
    return nodes
def lca(root, p, q):
    if root is None or root is p or root is q: return root
    L, R = lca(root.l, p, q), lca(root.r, p, q)
    return root if L and R else (L or R)
def path(root, target, acc=()):
    if root is None: return None
    acc = acc + (root,)
    if root is target: return acc
    return path(root.l, target, acc) or path(root.r, target, acc)
nodes = build(list(range(15)))
for _ in range(200):
    p, q = random.sample(nodes, 2)
    a, b = path(nodes[0], p), path(nodes[0], q)
    expected = [x for x, y in zip(a, b) if x is y][-1]
    assert lca(nodes[0], p, q) is expected
print("LCA verified on a 15-node tree")
