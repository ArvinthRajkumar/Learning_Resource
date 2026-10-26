def word_search(board, word):
    rows, cols = len(board), len(board[0])
    grid = [list(r) for r in board]
    def dfs(r, c, i):
        if i == len(word):
            return True
        if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] != word[i]:
            return False
        saved, grid[r][c] = grid[r][c], "#"          # choose
        found = (dfs(r + 1, c, i + 1) or dfs(r - 1, c, i + 1) or
                 dfs(r, c + 1, i + 1) or dfs(r, c - 1, i + 1))
        grid[r][c] = saved                           # un-choose
        return found
    return any(dfs(r, c, 0) for r in range(rows) for c in range(cols))
