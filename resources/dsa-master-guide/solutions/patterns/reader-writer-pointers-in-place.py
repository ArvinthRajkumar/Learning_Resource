def remove_value(nums, val):
    w = 0
    for x in nums:
        if x != val:
            nums[w] = x
            w += 1
    return w
