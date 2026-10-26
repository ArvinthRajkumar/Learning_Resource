def subsets(nums):
    res, path = [], []
    def backtrack(start):
        res.append(path[:])              # every path is a valid subset
        for i in range(start, len(nums)):
            path.append(nums[i])         # choose
            backtrack(i + 1)             # explore
            path.pop()                   # un-choose
    backtrack(0)
    return res
