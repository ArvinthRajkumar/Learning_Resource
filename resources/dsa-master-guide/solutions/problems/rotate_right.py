def rotate_right(nums, k):
    n = len(nums)
    if n == 0:
        return nums
    k %= n
    def rev(lo, hi):
        while lo < hi:
            nums[lo], nums[hi] = nums[hi], nums[lo]
            lo += 1
            hi -= 1
    rev(0, n - 1)       # whole list
    rev(0, k - 1)       # first k
    rev(k, n - 1)       # remaining
    return nums
