def is_pair_sum(nums, target):      # nums must be sorted
    lo, hi = 0, len(nums) - 1
    while lo < hi:
        s = nums[lo] + nums[hi]
        if s == target:
            return True
        if s < target:
            lo += 1                 # need a bigger sum
        else:
            hi -= 1                 # need a smaller sum
    return False
