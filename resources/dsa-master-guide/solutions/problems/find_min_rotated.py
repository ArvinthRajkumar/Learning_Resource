def find_min_rotated(nums):
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        mid = (lo + hi) // 2
        if nums[mid] > nums[hi]:
            lo = mid + 1        # minimum is in the right part
        else:
            hi = mid            # mid could be the minimum
    return nums[lo]
