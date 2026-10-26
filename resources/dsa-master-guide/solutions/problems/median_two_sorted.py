def median_two_sorted(a, b):
    if len(a) > len(b):
        a, b = b, a
    n, m = len(a), len(b)
    half = (n + m + 1) // 2
    lo, hi = 0, n
    INF = float("inf")
    while lo <= hi:
        i = (lo + hi) // 2            # elements taken from a
        j = half - i                  # elements taken from b
        a_left = a[i - 1] if i > 0 else -INF
        a_right = a[i] if i < n else INF
        b_left = b[j - 1] if j > 0 else -INF
        b_right = b[j] if j < m else INF
        if a_left <= b_right and b_left <= a_right:
            if (n + m) % 2:
                return float(max(a_left, b_left))
            return (max(a_left, b_left) + min(a_right, b_right)) / 2
        if a_left > b_right:
            hi = i - 1
        else:
            lo = i + 1
