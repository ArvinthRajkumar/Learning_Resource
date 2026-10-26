import random
random.seed(2)

class SegTree:
    """Iterative segment tree for any associative operation with an identity element."""
    def __init__(self, data, op, identity):
        self.n, self.op, self.id = len(data), op, identity
        self.t = [identity] * self.n + list(data)
        for i in range(self.n - 1, 0, -1):
            self.t[i] = op(self.t[2 * i], self.t[2 * i + 1])
    def update(self, i, v):
        i += self.n
        self.t[i] = v
        while i > 1:
            i //= 2
            self.t[i] = self.op(self.t[2 * i], self.t[2 * i + 1])
    def query(self, l, r):               # half-open [l, r)
        res_l, res_r = self.id, self.id
        l += self.n; r += self.n
        while l < r:
            if l & 1:
                res_l = self.op(res_l, self.t[l]); l += 1
            if r & 1:
                r -= 1; res_r = self.op(self.t[r], res_r)
            l //= 2; r //= 2
        return self.op(res_l, res_r)

data = [random.randint(-50, 50) for _ in range(37)]
mn = SegTree(data, min, float("inf"))
sm = SegTree(data, lambda x, y: x + y, 0)
for _ in range(3000):
    if random.random() < 0.4:
        i, v = random.randrange(37), random.randint(-50, 50)
        data[i] = v; mn.update(i, v); sm.update(i, v)
    else:
        l = random.randrange(37); r = random.randint(l + 1, 37)
        assert mn.query(l, r) == min(data[l:r]) and sm.query(l, r) == sum(data[l:r])
print("min and sum segment trees match brute force on 3000 operations")
