def permutations_unique(nums):
    nums.sort()
    res, path, used = [], [], [False] * len(nums)
    def go():
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and not used[i - 1]):
                continue
            used[i] = True; path.append(nums[i])
            go()
            used[i] = False; path.pop()
    go()
    return res
