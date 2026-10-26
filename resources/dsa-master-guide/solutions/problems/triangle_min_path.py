def triangle_min_path(tri):
    row = tri[-1][:]
    for r in range(len(tri) - 2, -1, -1):
        for c in range(len(tri[r])):
            row[c] = tri[r][c] + min(row[c], row[c + 1])
    return row[0]
