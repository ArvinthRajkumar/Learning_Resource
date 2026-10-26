def max_product_subarray(nums):
    hi = lo = best = nums[0]
    for x in nums[1:]:
        if x < 0:
            hi, lo = lo, hi               # a negative flips the order
        hi = max(x, hi * x)
        lo = min(x, lo * x)
        best = max(best, hi)
    return best
