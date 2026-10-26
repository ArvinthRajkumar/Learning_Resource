from itertools import accumulate
nums = [2, 4, 1, 3]
prefix = [0] + list(accumulate(nums))     # [0, 2, 6, 7, 10]
print(prefix[3] - prefix[1])              # sum of nums[1..2] = 4 + 1 = 5
