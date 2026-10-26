a, b = {1, 2, 3, 4}, {3, 4, 5}
print(a | b, a & b, a - b, a ^ b)
print(a <= {1, 2, 3, 4, 5}, 3 in a)
print(sorted(set("mississippi")))
dedup = list(dict.fromkeys([3, 1, 3, 2, 1]))   # remove duplicates, keep order
print(dedup)
