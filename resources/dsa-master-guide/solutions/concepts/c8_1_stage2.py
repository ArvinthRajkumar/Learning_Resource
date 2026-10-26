from bisect import bisect_left

def has_pair(nums, target):
    for i, x in enumerate(nums):
        j = bisect_left(nums, target - x, i + 1)
        if j < len(nums) and nums[j] == target - x:
            return True
    return False
