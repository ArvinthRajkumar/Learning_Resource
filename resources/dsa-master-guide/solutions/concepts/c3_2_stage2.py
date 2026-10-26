def missing_number(nums):
    s = set(nums)
    for v in range(len(nums) + 1):
        if v not in s:
            return v
