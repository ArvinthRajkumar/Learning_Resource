def rob(nums):
    skip, take = 0, 0
    for x in nums:
        skip, take = take, max(take, skip + x)
    return take
