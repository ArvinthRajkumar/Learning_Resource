def subsets_with_dup(nums):
    nums.sort()
    res, path = [], []
    def go(start):
        res.append(path[:])
        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue                  # skip duplicate at the same level
            path.append(nums[i])
            go(i + 1)
            path.pop()
    go(0)
    return res
