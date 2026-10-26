def diagonal_sum(m):
    n = len(m)
    total = sum(m[i][i] + m[i][n - 1 - i] for i in range(n))
    if n % 2 == 1:
        total -= m[n // 2][n // 2]    # centre counted twice
    return total
