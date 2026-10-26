def lower_bound(nums, target):
    lo, hi = 0, len(nums)            # hi = len, answer may be len
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < target:
            lo = mid + 1
        else:
            hi = mid                 # nums[mid] >= target could be the answer
    return lo
