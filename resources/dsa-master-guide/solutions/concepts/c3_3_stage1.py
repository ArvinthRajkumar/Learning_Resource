def max_subarray(nums):
    best = nums[0]
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            best = max(best, sum(nums[i:j + 1]))
    return best
