def n_queens(n):
    cols, d1, d2 = set(), set(), set()
    def go(r):
        if r == n: return 1
        total = 0
        for c in range(n):
            if c in cols or r - c in d1 or r + c in d2: continue
            cols.add(c); d1.add(r - c); d2.add(r + c)
            total += go(r + 1)
            cols.remove(c); d1.remove(r - c); d2.remove(r + c)
        return total
    return go(0)
known = {1: 1, 4: 2, 5: 10, 6: 4, 7: 40, 8: 92}
assert all(n_queens(n) == v for n, v in known.items())
print("n-queens counts match the known sequence:", [n_queens(n) for n in range(1, 9)])
