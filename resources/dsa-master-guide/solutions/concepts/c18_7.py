class Fenwick:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)         # 1-indexed

    def update(self, i, delta):           # add delta to position i (1-indexed)
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i

    def prefix(self, i):                  # sum of positions 1..i
        total = 0
        while i > 0:
            total += self.tree[i]
            i -= i & -i
        return total

    def range_sum(self, l, r):
        return self.prefix(r) - self.prefix(l - 1)
