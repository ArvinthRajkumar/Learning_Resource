col = [[1], [2], [3]]                              # shape (3, 1)
row = [[10, 20, 30, 40]]                           # shape (1, 4)
broadcast_sum = [[c[0] + r for r in row[0]] for c in col]       # result shape (3, 4)
print(broadcast_sum)
matrix = [[1, 2, 3], [4, 5, 6]]
col_sums = [sum(r[j] for r in matrix) for j in range(3)]        # like axis=0
row_sums = [sum(r) for r in matrix]                             # like axis=1
mean = [s / len(matrix) for s in col_sums]
centered = [[v - m for v, m in zip(r, mean)] for r in matrix]   # subtract each column's mean from its column
print(col_sums, row_sums, centered)
