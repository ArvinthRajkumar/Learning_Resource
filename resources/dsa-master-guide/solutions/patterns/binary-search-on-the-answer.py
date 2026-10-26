def smallest_feasible(lo, hi, can_do):
    while lo < hi:
        mid = (lo + hi) // 2
        if can_do(mid):
            hi = mid
        else:
            lo = mid + 1
    return lo
