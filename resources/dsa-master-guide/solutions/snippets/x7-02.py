import random
random.seed(1)
def product_except_self(a):
    n, out = len(a), [1] * len(a)
    left = 1
    for i in range(n):
        out[i] = left; left *= a[i]
    right = 1
    for i in range(n - 1, -1, -1):
        out[i] *= right; right *= a[i]
    return out
def brute(a):
    out = []
    for i in range(len(a)):
        p = 1
        for j, x in enumerate(a):
            if j != i: p *= x
        out.append(p)
    return out
for _ in range(200):
    a = [random.randint(-3, 3) for _ in range(random.randint(1, 8))]
    assert product_except_self(a) == brute(a)
print("verified;", product_except_self([1, 2, 3, 4]))
