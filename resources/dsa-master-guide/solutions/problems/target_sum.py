def target_sum(nums, target):
    total = sum(nums)
    if abs(target) > total or (total + target) % 2:
        return 0
    want = (total + target) // 2
    dp = [1] + [0] * want
    for x in nums:
        for s in range(want, x - 1, -1):
            dp[s] += dp[s - x]
    return dp[want]
