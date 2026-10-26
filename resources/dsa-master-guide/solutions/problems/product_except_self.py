def product_except_self(nums):
    n = len(nums)
    res = [1] * n
    left = 1
    for i in range(n):            # res[i] = product of everything to the left
        res[i] = left
        left *= nums[i]
    right = 1
    for i in range(n - 1, -1, -1):   # multiply by product of everything to the right
        res[i] *= right
        right *= nums[i]
    return res
