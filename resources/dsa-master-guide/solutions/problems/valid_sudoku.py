def valid_sudoku(board):
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = {}
    for r in range(9):
        for c in range(9):
            d = board[r][c]
            if d == ".":
                continue
            box = boxes.setdefault((r // 3, c // 3), set())
            if d in rows[r] or d in cols[c] or d in box:
                return False
            rows[r].add(d); cols[c].add(d); box.add(d)
    return True
