def has_duplicate(nums):
    nums = sorted(nums)
    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False
