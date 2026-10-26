def can_partition(nums):                 # subset sum: split into two equal-sum halves?
    total = sum(nums)
    if total % 2: return False
    target, reach = total // 2, {0}
    for x in nums:
        reach |= {r + x for r in reach if r + x <= target}
    return target in reach
def ways_combinations(coins, target):    # unordered: coins outer, amount inner
    dp = [1] + [0] * target
    for c in coins:
        for a in range(c, target + 1): dp[a] += dp[a - c]
    return dp[target]
def ways_permutations(coins, target):    # ordered: amount outer, coins inner
    dp = [1] + [0] * target
    for a in range(1, target + 1):
        for c in coins:
            if c <= a: dp[a] += dp[a - c]
    return dp[target]
print(can_partition([1, 5, 11, 5]), can_partition([1, 2, 3, 5]))
print("combinations:", ways_combinations([1, 2, 5], 5), "| ordered sequences:", ways_permutations([1, 2, 5], 5))
