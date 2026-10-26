def min_eating_speed(piles, h):
    def hours(speed):
        return sum((p + speed - 1) // speed for p in piles)   # ceil(p / speed)
    lo, hi = 1, max(piles)
    while lo < hi:
        mid = (lo + hi) // 2
        if hours(mid) <= h:
            hi = mid          # fast enough, try slower
        else:
            lo = mid + 1      # too slow
    return lo
