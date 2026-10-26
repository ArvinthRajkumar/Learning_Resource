def game_of_life(board):
    R, C = len(board), len(board[0])
    out = [[0] * C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            live = sum(board[r + dr][c + dc]
                       for dr in (-1, 0, 1) for dc in (-1, 0, 1)
                       if (dr or dc) and 0 <= r + dr < R and 0 <= c + dc < C)
            out[r][c] = 1 if live == 3 or (board[r][c] and live == 2) else 0
    return out
