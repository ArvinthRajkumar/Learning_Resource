def combination_sum(candidates, target):
    candidates.sort()
    res, path = [], []
    def backtrack(start, remain):
        if remain == 0:
            res.append(path[:])
            return
        for i in range(start, len(candidates)):
            if candidates[i] > remain:
                break                    # all later ones are bigger too
            path.append(candidates[i])
            backtrack(i, remain - candidates[i])
            path.pop()
    backtrack(0, target)
    return res
