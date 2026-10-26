def max_area(h):
    lo, hi, best = 0, len(h) - 1, 0
    while lo < hi:
        best = max(best, (hi - lo) * min(h[lo], h[hi]))
        if h[lo] < h[hi]:
            lo += 1
        else:
            hi -= 1
    return best
