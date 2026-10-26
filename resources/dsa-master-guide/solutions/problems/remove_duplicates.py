def remove_duplicates(nums):
    if not nums:
        return 0
    w = 1
    for r in range(1, len(nums)):
        if nums[r] != nums[w - 1]:   # a new value
            nums[w] = nums[r]
            w += 1
    return w
