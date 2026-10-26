import random
random.seed(15)
def kadane(a, f=max):
    best = cur = a[0]
    for x in a[1:]:
        cur = f(x, cur + x); best = f(best, cur)
    return best
def circular(a):
    mx, mn, total = kadane(a), kadane(a, min), sum(a)
    return mx if mx < 0 else max(mx, total - mn)
def brute(a):
    n = len(a)
    return max(sum(a[(i + k) % n] for k in range(L)) for i in range(n) for L in range(1, n + 1))
for _ in range(300):
    a = [random.randint(-5, 5) for _ in range(random.randint(1, 9))]
    assert circular(a) == brute(a)
print("circular Kadane verified")
