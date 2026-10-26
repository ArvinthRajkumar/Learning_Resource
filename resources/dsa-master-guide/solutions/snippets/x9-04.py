import random
random.seed(4)
def max_sub(a, lo, hi):
    if lo == hi: return a[lo]
    mid = (lo + hi) // 2
    best_left, best_right = max_sub(a, lo, mid), max_sub(a, mid + 1, hi)
    s, left_best = 0, float("-inf")
    for i in range(mid, lo - 1, -1): s += a[i]; left_best = max(left_best, s)
    s, right_best = 0, float("-inf")
    for i in range(mid + 1, hi + 1): s += a[i]; right_best = max(right_best, s)
    return max(best_left, best_right, left_best + right_best)
for _ in range(300):
    a = [random.randint(-6, 6) for _ in range(random.randint(1, 12))]
    brute = max(sum(a[i:j]) for i in range(len(a)) for j in range(i + 1, len(a) + 1))
    assert max_sub(a, 0, len(a) - 1) == brute
print("divide-and-conquer maximum subarray verified")
