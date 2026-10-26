def find_peak(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] < nums[mid + 1]:
            lo = mid + 1        # uphill: peak on the right
        else:
            hi = mid            # downhill: peak at mid or left
    return lo
