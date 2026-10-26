def two_city_cost(costs):
    costs = sorted(costs, key=lambda c: c[0] - c[1])
    n = len(costs) // 2
    return sum(c[0] for c in costs[:n]) + sum(c[1] for c in costs[n:])
