def unique_bst(n):
    dp = [1, 1] + [0] * (n - 1)
    for nodes in range(2, n + 1):
        for root in range(1, nodes + 1):
            dp[nodes] += dp[root - 1] * dp[nodes - root]
    return dp[n]
