import random
random.seed(0)
def ks(a, b):
    a, b = sorted(a), sorted(b)
    pts = sorted(set(a + b))
    def cdf(s, x):
        lo, hi = 0, len(s)
        while lo < hi:
            mid = (lo + hi) // 2
            if s[mid] <= x: lo = mid + 1
            else: hi = mid
        return lo / len(s)
    return max(abs(cdf(a, x) - cdf(b, x)) for x in pts)
ref = [random.gauss(0, 1) for _ in range(2000)]
same = [random.gauss(0, 1) for _ in range(2000)]
moved = [random.gauss(0.5, 1) for _ in range(2000)]
print("KS same distribution : %.3f" % ks(ref, same))
print("KS shifted by 0.5    : %.3f" % ks(ref, moved))
