import math, random
random.seed(1)
class SqrtArray:
    def __init__(self, a):
        self.a, self.B = a[:], max(1, int(math.sqrt(len(a))))
        self.sums = [sum(a[i:i + self.B]) for i in range(0, len(a), self.B)]
    def update(self, i, v):
        self.sums[i // self.B] += v - self.a[i]; self.a[i] = v
    def query(self, l, r):                                    # inclusive range sum
        total, B = 0, self.B
        while l <= r and l % B != 0: total += self.a[l]; l += 1          # left partial block
        while l + B - 1 <= r: total += self.sums[l // B]; l += B          # whole blocks
        while l <= r: total += self.a[l]; l += 1                          # right partial block
        return total
a = [random.randint(-9, 9) for _ in range(500)]
sa = SqrtArray(a)
for _ in range(2000):
    if random.random() < 0.3:
        i, v = random.randrange(500), random.randint(-9, 9); sa.update(i, v); a[i] = v
    else:
        l = random.randrange(500); r = random.randrange(l, 500); assert sa.query(l, r) == sum(a[l:r + 1])
print(f"sqrt decomposition (block size {sa.B}) matches brute force on 2000 mixed operations")
