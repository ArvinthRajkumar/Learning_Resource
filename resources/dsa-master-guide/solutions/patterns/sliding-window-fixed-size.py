def best_window(nums, k):
    w = sum(nums[:k])
    best = w
    for i in range(k, len(nums)):
        w += nums[i] - nums[i - k]
        best = max(best, w)
    return best
