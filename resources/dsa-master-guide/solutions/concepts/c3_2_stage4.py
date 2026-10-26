def missing_number(nums):
    x = len(nums)
    for i, v in enumerate(nums):
        x ^= i ^ v
    return x
