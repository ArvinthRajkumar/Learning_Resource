def house_robber(nums):
    skip, take = 0, 0              # best up to i-2, best up to i-1
    for x in nums:
        skip, take = take, max(take, skip + x)
    return take
