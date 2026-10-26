def subarrays_div_k(nums, k):
    counts = {0: 1}
    prefix = ans = 0
    for x in nums:
        prefix = (prefix + x) % k
        ans += counts.get(prefix, 0)
        counts[prefix] = counts.get(prefix, 0) + 1
    return ans
