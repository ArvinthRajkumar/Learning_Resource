long = [("ana", "q1", 10), ("ana", "q2", 15), ("bo", "q1", 7), ("bo", "q2", 9), ("bo", "q3", 12)]
quarters = sorted({q for _, q, _ in long})
wide = {}
for name, q, v in long: wide.setdefault(name, dict.fromkeys(quarters)); wide[name][q] = v
print("wide:", wide)
melted = [(name, q, v) for name, cols in wide.items() for q, v in cols.items() if v is not None]
print("back to long:", melted == sorted(long) or sorted(melted) == sorted(long))
