grid = [[0] * 3] * 2          # two references to the SAME row!
grid[0][0] = 1
print(grid)
grid = [[0] * 3 for _ in range(2)]   # correct
grid[0][0] = 1
print(grid)
