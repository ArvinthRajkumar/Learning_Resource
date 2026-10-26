def subsets_bitmask(nums):
    n = len(nums)
    res = []
    for mask in range(1 << n):
        res.append([nums[i] for i in range(n) if (mask >> i) & 1])
    return res
