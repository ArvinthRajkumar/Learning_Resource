def permutations(nums):
    res, path = [], []
    used = [False] * len(nums)
    def backtrack():
        if len(path) == len(nums):
            res.append(path[:])
            return
        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True; path.append(nums[i])    # choose
            backtrack()
            used[i] = False; path.pop()             # un-choose
    backtrack()
    return res
