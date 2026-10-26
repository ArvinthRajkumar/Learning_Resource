def can_make(nums, target):
    reach = [True] + [False] * target
    for x in nums:
        for s in range(target, x - 1, -1):
            if reach[s - x]:
                reach[s] = True
    return reach[target]
