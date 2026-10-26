def total_copy_cost(n, factor=2):
    cap, size, cost = 1, 0, 0
    for _ in range(n):
        if size == cap:
            cost += size            # copy all elements
            cap = max(cap + 1, int(cap * factor))
        size += 1
        cost += 1                   # the append itself
    return cost
for n in [10**3, 10**4, 10**5]:
    print(f"n = {n:>6}: total cost / n = {total_copy_cost(n) / n:.2f} (doubling) vs {total_copy_cost(n, 1.0) / n:.1f} (grow by +1)")
