def count_divisible(nums, k):
    count = 0
    for x in nums:
        if x % k == 0:      # x is divisible by k
            count += 1
    return count
