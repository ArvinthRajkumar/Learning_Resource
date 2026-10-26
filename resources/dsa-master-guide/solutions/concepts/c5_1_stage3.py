from bisect import bisect_left

def search(nums, target):
    i = bisect_left(nums, target)
    return i if i < len(nums) and nums[i] == target else -1
