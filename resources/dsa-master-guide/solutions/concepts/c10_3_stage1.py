def next_greater(nums):
    res = []
    for i, x in enumerate(nums):
        for y in nums[i + 1:]:
            if y > x:
                res.append(y)
                break
        else:
            res.append(-1)
    return res
