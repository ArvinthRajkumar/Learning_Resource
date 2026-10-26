def set_matrix_zeroes(matrix):
    zero_rows, zero_cols = set(), set()
    for r, row in enumerate(matrix):
        for c, v in enumerate(row):
            if v == 0:
                zero_rows.add(r)
                zero_cols.add(c)
    for r in range(len(matrix)):
        for c in range(len(matrix[0])):
            if r in zero_rows or c in zero_cols:
                matrix[r][c] = 0
    return matrix
