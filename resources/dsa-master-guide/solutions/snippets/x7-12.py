import random, itertools
from collections import deque
random.seed(11)
def can_finish(n, pre):
    g, indeg = [[] for _ in range(n)], [0] * n
    for a, b in pre: g[b].append(a); indeg[a] += 1
    q, seen = deque(i for i in range(n) if indeg[i] == 0), 0
    while q:
        u = q.popleft(); seen += 1
        for v in g[u]:
            indeg[v] -= 1
            if indeg[v] == 0: q.append(v)
    return seen == n
def brute(n, pre):
    return any(all(pos[b] < pos[a] for a, b in pre) for perm in itertools.permutations(range(n)) for pos in [{v: i for i, v in enumerate(perm)}])
for _ in range(300):
    n = random.randint(1, 5)
    pre = [(random.randrange(n), random.randrange(n)) for _ in range(random.randint(0, 6))]
    assert can_finish(n, pre) == brute(n, pre)
print("verified;", can_finish(2, [(1, 0)]), can_finish(2, [(1, 0), (0, 1)]))
