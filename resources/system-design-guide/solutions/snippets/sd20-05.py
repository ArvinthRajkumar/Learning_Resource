import random, hashlib
random.seed(2)
class CountMin:
    def __init__(self, w=500, d=4): self.w, self.d, self.t = w, d, [[0] * w for _ in range(d)]
    def _h(self, x, i): return int(hashlib.md5(f"{i}{x}".encode()).hexdigest(), 16) % self.w
    def add(self, x):
        for i in range(self.d): self.t[i][self._h(x, i)] += 1
    def est(self, x): return min(self.t[i][self._h(x, i)] for i in range(self.d))
stream = [f"u{min(int(random.paretovariate(1.2)), 2000)}" for _ in range(20000)]
cm, exact = CountMin(), {}
for x in stream:
    cm.add(x); exact[x] = exact.get(x, 0) + 1
top = sorted(exact, key=exact.get, reverse=True)[:3]
print([(u, exact[u], cm.est(u)) for u in top], "(item, exact, estimate); estimates never undercount:", all(cm.est(u) >= exact[u] for u in exact))
