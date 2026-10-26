def house_robber_ii(nums):
    def line(a):
        skip, take = 0, 0
        for x in a:
            skip, take = take, max(take, skip + x)
        return take
    if len(nums) == 1:
        return nums[0]
    return max(line(nums[1:]), line(nums[:-1]))
