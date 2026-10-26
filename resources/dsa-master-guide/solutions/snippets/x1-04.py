import random
random.seed(3)

class LazySum:
    def __init__(self, n):
        self.n = n
        self.sum = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
    def _push(self, node, lo, hi):
        if self.lazy[node]:
            mid = (lo + hi) // 2
            for child, clo, chi in ((2 * node, lo, mid), (2 * node + 1, mid + 1, hi)):
                self.sum[child] += self.lazy[node] * (chi - clo + 1)
                self.lazy[child] += self.lazy[node]
            self.lazy[node] = 0
    def add(self, l, r, v, node=1, lo=0, hi=None):
        hi = self.n - 1 if hi is None else hi
        if r < lo or hi < l: return
        if l <= lo and hi <= r:
            self.sum[node] += v * (hi - lo + 1)
            self.lazy[node] += v
            return
        self._push(node, lo, hi)
        mid = (lo + hi) // 2
        self.add(l, r, v, 2 * node, lo, mid)
        self.add(l, r, v, 2 * node + 1, mid + 1, hi)
        self.sum[node] = self.sum[2 * node] + self.sum[2 * node + 1]
    def query(self, l, r, node=1, lo=0, hi=None):
        hi = self.n - 1 if hi is None else hi
        if r < lo or hi < l: return 0
        if l <= lo and hi <= r: return self.sum[node]
        self._push(node, lo, hi)
        mid = (lo + hi) // 2
        return self.query(l, r, 2 * node, lo, mid) + self.query(l, r, 2 * node + 1, mid + 1, hi)

n = 40
arr = [0] * n
t = LazySum(n)
for _ in range(2000):
    l = random.randrange(n); r = random.randint(l, n - 1)
    if random.random() < 0.5:
        v = random.randint(-4, 4)
        for i in range(l, r + 1): arr[i] += v
        t.add(l, r, v)
    else:
        assert t.query(l, r) == sum(arr[l:r + 1])
print("lazy segment tree matches brute force")
