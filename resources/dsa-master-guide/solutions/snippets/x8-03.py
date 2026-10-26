import random
random.seed(3)
n = 40
parent = [-1] + [random.randrange(i) for i in range(1, n)]
children = [[] for _ in range(n)]
for v in range(1, n): children[parent[v]].append(v)
tin, tout, timer = [0] * n, [0] * n, 0
stack = [(0, 0)]
while stack:                                                           # iterative DFS with enter/exit events
    v, state = stack.pop()
    if state == 0:
        tin[v] = timer; timer += 1
        stack.append((v, 1))
        for c in children[v]: stack.append((c, 0))
    else:
        tout[v] = timer
class Fenwick:
    def __init__(self, n): self.t = [0] * (n + 1)
    def add(self, i, d):
        i += 1
        while i < len(self.t): self.t[i] += d; i += i & -i
    def prefix(self, i):                                               # sum of [0, i)
        s = 0
        while i > 0: s += self.t[i]; i -= i & -i
        return s
values = [random.randint(1, 9) for _ in range(n)]
fw = Fenwick(n)
for v in range(n): fw.add(tin[v], values[v])
def subtree_sum(v): return fw.prefix(tout[v]) - fw.prefix(tin[v])
def subtree_sum_naive(v):
    return values[v] + sum(subtree_sum_naive(c) for c in children[v])
for _ in range(100):
    v = random.randrange(n); assert subtree_sum(v) == subtree_sum_naive(v)
for _ in range(100):                                                   # point updates, then re-check
    v, d = random.randrange(n), random.randint(-5, 5)
    values[v] += d; fw.add(tin[v], d)
    w = random.randrange(n); assert subtree_sum(w) == subtree_sum_naive(w)
print("subtree sums with point updates verified against recursion; root subtree sum:", subtree_sum(0), "=", sum(values))
