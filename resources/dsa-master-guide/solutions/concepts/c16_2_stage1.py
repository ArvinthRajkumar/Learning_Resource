def rob(nums, i=0):
    if i >= len(nums):
        return 0
    return max(nums[i] + rob(nums, i + 2), rob(nums, i + 1))
