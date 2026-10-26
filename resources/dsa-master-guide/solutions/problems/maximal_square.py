def maximal_square(matrix):
    if not matrix:
        return 0
    R, C = len(matrix), len(matrix[0])
    dp = [[0] * (C + 1) for _ in range(R + 1)]
    best = 0
    for r in range(1, R + 1):
        for c in range(1, C + 1):
            if matrix[r - 1][c - 1] == "1":
                dp[r][c] = 1 + min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1])
                best = max(best, dp[r][c])
    return best * best
