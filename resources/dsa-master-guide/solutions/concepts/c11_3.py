def n_queens(n):
    cols, d1, d2 = set(), set(), set()
    count = 0
    def place(row):
        nonlocal count
        if row == n:
            count += 1
            return
        for c in range(n):
            if c in cols or row - c in d1 or row + c in d2:
                continue                       # pruned: attacked
            cols.add(c); d1.add(row - c); d2.add(row + c)
            place(row + 1)
            cols.remove(c); d1.remove(row - c); d2.remove(row + c)
    place(0)
    return count
