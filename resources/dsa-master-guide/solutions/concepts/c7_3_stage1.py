def longest(nums):
    nums = sorted(set(nums))
    best = cur = 1 if nums else 0
    for i in range(1, len(nums)):
        cur = cur + 1 if nums[i] == nums[i - 1] + 1 else 1
        best = max(best, cur)
    return best
