import random
random.seed(4)
a = [random.randint(0, 99) for _ in range(40)]
n = len(a)
LOG = [0] * (n + 1)
for i in range(2, n + 1):
    LOG[i] = LOG[i // 2] + 1
table = [a[:]]
k = 1
while (1 << k) <= n:
    prev = table[-1]
    table.append([min(prev[i], prev[i + (1 << (k - 1))]) for i in range(n - (1 << k) + 1)])
    k += 1
def rmq(l, r):                              # inclusive
    k = LOG[r - l + 1]
    return min(table[k][l], table[k][r - (1 << k) + 1])
assert all(rmq(l, r) == min(a[l:r + 1]) for l in range(n) for r in range(l, n))
print("sparse table verified on all", n * (n + 1) // 2, "ranges; levels:", len(table))
