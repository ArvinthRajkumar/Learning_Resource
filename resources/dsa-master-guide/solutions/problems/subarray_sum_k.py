def subarray_sum_k(nums, k):
    counts = {0: 1}          # prefix sum -> times seen
    prefix = total = 0
    for x in nums:
        prefix += x
        total += counts.get(prefix - k, 0)
        counts[prefix] = counts.get(prefix, 0) + 1
    return total
