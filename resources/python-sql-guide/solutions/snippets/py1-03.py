ages = {"ada": 36, "bob": 25}
ages["cy"] = 41
print(ages["ada"], ages.get("zed"), ages.get("zed", 0))
for name, age in ages.items():
    print(name, age)
print(list(ages), list(ages.values()), "bob" in ages)
del ages["bob"]
print(ages.pop("cy"), ages)
merged = {"a": 1} | {"b": 2}
print(merged)
