def next_greater(nums):
    ans, stack = [-1] * len(nums), []                       # stack holds indexes still waiting for a taller element
    for i, x in enumerate(nums):
        while stack and nums[stack[-1]] < x: ans[stack.pop()] = x
        stack.append(i)
    return ans
print(next_greater([2, 1, 2, 4, 3]), "(each element is pushed and popped once, so O(n))")
