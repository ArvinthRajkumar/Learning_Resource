nums = [1, 2, 3, 4, 5, 6]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)               # skips elements!
print(nums)
print([n for n in [1, 2, 3, 4, 5, 6] if n % 2])   # correct
