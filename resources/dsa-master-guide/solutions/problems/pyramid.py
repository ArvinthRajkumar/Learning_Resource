def pyramid(n):
    lines = []
    for i in range(1, n + 1):
        row = [str(j) for j in range(1, i + 1)]
        lines.append(" ".join(row))
    return lines
