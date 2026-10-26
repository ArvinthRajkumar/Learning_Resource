def ship_capacity(weights, days):
    def can_ship(cap):
        need, load = 1, 0
        for w in weights:
            if load + w > cap:      # start a new day
                need += 1
                load = 0
            load += w
        return need <= days
    lo, hi = max(weights), sum(weights)
    while lo < hi:
        mid = (lo + hi) // 2
        if can_ship(mid):
            hi = mid                # try smaller
        else:
            lo = mid + 1
    return lo
