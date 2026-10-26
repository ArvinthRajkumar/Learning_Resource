rows = [{"age": 34, "country": "US", "amount": 120.0}, {"age": -5, "country": "US", "amount": 80.0},
        {"age": 41, "country": "ZZ", "amount": None}, {"age": 29, "country": "FR", "amount": 55.5}]
allowed = {"US", "FR", "DE"}
errors = []
for i, r in enumerate(rows):
    if not (0 <= r["age"] <= 120): errors.append((i, "age out of range"))
    if r["country"] not in allowed: errors.append((i, "unknown country"))
    if r["amount"] is None: errors.append((i, "missing amount"))
print(errors)
