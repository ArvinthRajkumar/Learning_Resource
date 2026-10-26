grid = ["#..", ".#.", "..#"]
R, C = len(grid), len(grid[0])
DIRS = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def neighbours(r, c):
    for dr, dc in DIRS:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C: yield nr, nc
print(list(neighbours(0, 0)), "| transpose:", ["".join(col) for col in zip(*grid)], "| matrix without shared rows:", [[0] * 3 for _ in range(2)])
bad = [[0] * 3] * 2; bad[0][0] = 1
print("the aliasing trap [[0]*3]*2:", bad)
