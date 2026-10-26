def reverse_in_place(a):
    lo, hi = 0, len(a) - 1
    while lo < hi:
        a[lo], a[hi] = a[hi], a[lo]   # swap ends
        lo += 1
        hi -= 1
    return a
