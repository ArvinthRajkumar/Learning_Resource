def max_sum_window(nums, k):
    if k > len(nums):
        return -1
    window = sum(nums[:k])            # first window
    best = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]   # slide by one
        best = max(best, window)
    return best
