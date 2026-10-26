import random
random.seed(12)
def search_rotated(a, t):
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if a[mid] == t: return mid
        if a[lo] <= a[mid]:
            if a[lo] <= t < a[mid]: hi = mid - 1
            else: lo = mid + 1
        else:
            if a[mid] < t <= a[hi]: lo = mid + 1
            else: hi = mid - 1
    return -1
def find_min(a):
    lo, hi = 0, len(a) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] > a[hi]: lo = mid + 1
        else: hi = mid
    return a[lo]
for _ in range(300):
    base = sorted(random.sample(range(40), random.randint(1, 10)))
    k = random.randrange(len(base))
    a = base[k:] + base[:k]
    t = random.randint(-1, 41)
    got = search_rotated(a, t)
    assert (got == -1 and t not in a) or a[got] == t
    assert find_min(a) == min(a)
print("rotated search and min verified")
