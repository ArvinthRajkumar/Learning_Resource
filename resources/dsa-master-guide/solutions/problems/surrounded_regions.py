def surrounded_regions(board):
    grid = [list(r) for r in board]
    R, C = len(grid), len(grid[0])
    def mark(r, c):
        if 0 <= r < R and 0 <= c < C and grid[r][c] == "O":
            grid[r][c] = "S"                     # safe
            mark(r + 1, c); mark(r - 1, c); mark(r, c + 1); mark(r, c - 1)
    for r in range(R):
        mark(r, 0); mark(r, C - 1)
    for c in range(C):
        mark(0, c); mark(R - 1, c)
    return ["".join("O" if ch == "S" else "X" for ch in row) for row in grid]
