def knapsack_01(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for wt, val in zip(weights, values):
        for w in range(capacity, wt - 1, -1):     # backwards = use item once
            dp[w] = max(dp[w], dp[w - wt] + val)
    return dp[capacity]
