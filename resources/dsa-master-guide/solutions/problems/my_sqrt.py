def my_sqrt(x):
    lo, hi, ans = 0, x, 0
    while lo <= hi:
        mid = (lo + hi) // 2
        if mid * mid <= x:
            ans = mid          # mid works, try bigger
            lo = mid + 1
        else:
            hi = mid - 1
    return ans
