import random, itertools, bisect
random.seed(6)
def subset_sums(items):
    sums = [0]
    for x in items: sums += [s + x for s in sums]
    return sums
def closest_subset_sum(items, target):
    half = len(items) // 2
    A, B = subset_sums(items[:half]), sorted(subset_sums(items[half:]))
    best = None
    for a in A:
        j = bisect.bisect_left(B, target - a)
        for k in (j - 1, j):                                          # neighbours of the ideal partner
            if 0 <= k < len(B):
                cand = a + B[k]
                if best is None or abs(cand - target) < abs(best - target): best = cand
    return best
for _ in range(200):
    items = [random.randint(-20, 40) for _ in range(random.randint(1, 12))]; target = random.randint(-30, 100)
    brute = min((sum(c) for r in range(len(items) + 1) for c in itertools.combinations(items, r)), key=lambda s: (abs(s - target), s))
    assert abs(closest_subset_sum(items, target) - target) == abs(brute - target)
big = [random.randint(1, 10**6) for _ in range(30)]
print("meet in the middle verified | 30 items solved with", 2 ** 15 * 2, "enumerated sums instead of", 2 ** 30, "| closest sum to 7,000,000:", closest_subset_sum(big, 7_000_000))
