people = [("ada", 36), ("bob", 25), ("cy", 36)]
print(sorted(people, key=lambda p: p[1]))
print(sorted(people, key=lambda p: (-p[1], p[0])))      # age desc, then name asc
print(sorted(["b", "A", "c"], key=str.lower), sorted([3, 1, 2], reverse=True))
