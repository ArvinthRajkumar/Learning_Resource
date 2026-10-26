def unique_paths_obstacles(grid):
    R, C = len(grid), len(grid[0])
    dp = [0] * C
    dp[0] = 1 if grid[0][0] == 0 else 0
    for r in range(R):
        for c in range(C):
            if grid[r][c] == 1:
                dp[c] = 0
            elif c > 0:
                dp[c] += dp[c - 1]
    return dp[-1]
