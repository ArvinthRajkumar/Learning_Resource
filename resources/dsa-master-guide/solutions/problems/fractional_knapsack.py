def fractional_knapsack(values, weights, W):
    items = sorted(zip(values, weights), key=lambda p: p[0] / p[1], reverse=True)
    total = 0.0
    for v, w in items:
        if W >= w:
            total += v
            W -= w
        else:
            total += v * W / w     # take a fraction
            break
    return total
