def perfect_squares(n):
    dp = [0] + [float("inf")] * n
    for i in range(1, n + 1):
        s = 1
        while s * s <= i:
            dp[i] = min(dp[i], dp[i - s * s] + 1)
            s += 1
    return dp[n]
