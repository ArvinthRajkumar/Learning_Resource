def next_greater(nums):
    res = [-1] * len(nums)
    stack = []                      # indices waiting for a greater value
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x:
            res[stack.pop()] = x
        stack.append(i)
    return res
