from itertools import combinations
nodes = range(5)
majorities = [set(c) for c in combinations(nodes, 3)]
print("every pair of 3-of-5 majorities overlaps:", all(a & b for a in majorities for b in majorities))
print("two disjoint minorities of 2-of-5 exist (so 2 acks would be unsafe):", any(not (set(a) & set(b)) for a in combinations(nodes, 2) for b in combinations(nodes, 2)))
