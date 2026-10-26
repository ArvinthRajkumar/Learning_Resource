import random
random.seed(1)

class Fenwick:
    def __init__(self, n):
        self.n, self.t = n, [0] * (n + 1)
    def add(self, i, delta):              # 1-based index
        while i <= self.n:
            self.t[i] += delta
            i += i & -i
    def prefix(self, i):                  # sum of a[1..i]
        s = 0
        while i > 0:
            s += self.t[i]
            i -= i & -i
        return s
    def range_sum(self, l, r):            # inclusive, 1-based
        return self.prefix(r) - self.prefix(l - 1)

n = 50
a = [0] * (n + 1)
f = Fenwick(n)
for _ in range(2000):
    if random.random() < 0.5:
        i, d = random.randint(1, n), random.randint(-5, 5)
        a[i] += d; f.add(i, d)
    else:
        l = random.randint(1, n); r = random.randint(l, n)
        assert f.range_sum(l, r) == sum(a[l:r + 1])
print("2000 random operations match brute force")
print("lowest set bits:", [(i, i & -i) for i in (1, 2, 3, 4, 6, 8, 12)])
