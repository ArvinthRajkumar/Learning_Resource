import random
random.seed(5)
def min_largest_sum(nums, k):
    """Split nums into k contiguous parts to minimise the largest part sum."""
    def feasible(limit):
        parts, cur = 1, 0
        for x in nums:
            if x > limit: return False
            if cur + x > limit: parts += 1; cur = x
            else: cur += x
        return parts <= k
    lo, hi = max(nums), sum(nums)
    while lo < hi:
        mid = (lo + hi) // 2
        if feasible(mid): hi = mid
        else: lo = mid + 1
    return lo
def brute(nums, k):
    from itertools import combinations
    n, best = len(nums), float("inf")
    for cuts in combinations(range(1, n), k - 1):
        bounds = (0,) + cuts + (n,)
        best = min(best, max(sum(nums[bounds[i]:bounds[i + 1]]) for i in range(k)))
    return best
for _ in range(300):
    nums = [random.randint(1, 9) for _ in range(random.randint(1, 8))]; k = random.randint(1, len(nums))
    assert min_largest_sum(nums, k) == brute(nums, k)
print("binary search on the answer verified | [7,2,5,10,8] into 2 parts:", min_largest_sum([7, 2, 5, 10, 8], 2))
