import itertools
orders = {"o1": (3, 0), "o2": (0, 0)}
couriers = {"c1": (1, 0), "c2": (7, 0)}
dist = lambda a, b: abs(a[0] - b[0]) + abs(a[1] - b[1])
# greedy: process orders in arrival order, give each the nearest free courier
free, greedy = dict(couriers), {}
for o, loc in orders.items():
    c = min(free, key=lambda c: dist(free[c], loc)); greedy[o] = c; free.pop(c)
greedy_cost = sum(dist(orders[o], couriers[c]) for o, c in greedy.items())
# optimal assignment by brute force over permutations (Hungarian does this in O(n^3) for large n)
best = min(itertools.permutations(couriers), key=lambda perm: sum(dist(orders[o], couriers[c]) for o, c in zip(orders, perm)))
best_cost = sum(dist(orders[o], couriers[c]) for o, c in zip(orders, best))
print("greedy:", greedy, "total distance", greedy_cost)
print("batched optimal:", dict(zip(orders, best)), "total distance", best_cost)
