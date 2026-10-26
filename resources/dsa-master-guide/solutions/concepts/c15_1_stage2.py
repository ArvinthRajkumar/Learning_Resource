def coins(c, amount):
    INF = float('inf')
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for x in c:
            if x <= a:
                dp[a] = min(dp[a], dp[a - x] + 1)
    return -1 if dp[amount] == INF else dp[amount]
