def subset_sum_bitset(nums, target):
    bits = 1                                     # bit i set means sum i is reachable
    for x in nums:
        bits |= bits << x
    return bool(bits >> target & 1)
print(subset_sum_bitset([3, 34, 4, 12, 5, 2], 9), subset_sum_bitset([3, 34, 4, 12, 5, 2], 30))
