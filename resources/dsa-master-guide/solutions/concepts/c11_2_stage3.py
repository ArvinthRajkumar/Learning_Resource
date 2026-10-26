def subsets(nums):
    n = len(nums)
    return [[nums[i] for i in range(n) if m >> i & 1] for m in range(1 << n)]
