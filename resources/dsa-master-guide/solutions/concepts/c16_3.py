def lcs(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            if a[i - 1] == b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1           # extend a match
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  # skip a character
    return dp[-1][-1]

def knapsack(weights, values, capacity):
    dp = [0] * (capacity + 1)
    for wt, val in zip(weights, values):
        for w in range(capacity, wt - 1, -1):    # backwards: use each item once
            dp[w] = max(dp[w], dp[w - wt] + val)
    return dp[capacity]
