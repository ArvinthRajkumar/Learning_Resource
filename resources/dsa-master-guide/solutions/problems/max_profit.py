def max_profit(prices):
    lowest, best = float("inf"), 0
    for p in prices:
        lowest = min(lowest, p)          # cheapest buy so far
        best = max(best, p - lowest)     # profit if we sell today
    return best
