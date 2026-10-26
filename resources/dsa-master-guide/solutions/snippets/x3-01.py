from functools import lru_cache
import itertools, random
random.seed(0)

def coin_change_dp(coins, target):                    # minimum coins, bottom-up
    INF = float("inf")
    dp = [0] + [INF] * target
    for amount in range(1, target + 1):
        for c in coins:
            if c <= amount and dp[amount - c] + 1 < dp[amount]:
                dp[amount] = dp[amount - c] + 1
    return dp[target] if dp[target] != INF else -1

def coin_change_brute(coins, target):
    best = [float("inf")]
    def go(rem, used):
        if rem == 0: best[0] = min(best[0], used); return
        for c in coins:
            if c <= rem and used + 1 < best[0]: go(rem - c, used + 1)
    go(target, 0)
    return best[0] if best[0] != float("inf") else -1

for _ in range(60):
    coins = random.sample(range(1, 9), random.randint(1, 4))
    t = random.randint(0, 18)
    assert coin_change_dp(coins, t) == coin_change_brute(coins, t)
print("coin change DP matches brute force; example:", coin_change_dp([1, 5, 6, 9], 11))
