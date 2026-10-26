def count_subarrays(nums, k):
    seen, pre, ans = {0: 1}, 0, 0
    for x in nums:
        pre += x
        ans += seen.get(pre - k, 0)
        seen[pre] = seen.get(pre, 0) + 1
    return ans
