def move_zeroes(nums):
    w = 0                           # next slot for a non-zero value
    for x in nums:
        if x != 0:
            nums[w] = x
            w += 1
    for i in range(w, len(nums)):   # fill the rest with zeros
        nums[i] = 0
    return nums
