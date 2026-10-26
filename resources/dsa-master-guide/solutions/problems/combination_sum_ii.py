def combination_sum_ii(candidates, target):
    candidates.sort()
    res, path = [], []
    def go(start, remain):
        if remain == 0:
            res.append(path[:])
            return
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            if candidates[i] > remain:
                break
            path.append(candidates[i])
            go(i + 1, remain - candidates[i])
            path.pop()
    go(0, target)
    return res
