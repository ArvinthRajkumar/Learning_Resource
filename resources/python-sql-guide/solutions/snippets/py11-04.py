import random
def my_sort(xs):                                       # code under test (a deliberately buggy variant is below)
    return sorted(xs)
def buggy_sort(xs):
    out = sorted(set(xs))                              # bug: drops duplicates
    return out
def check_sort_properties(sort, trials=500, seed=0):
    rng = random.Random(seed)
    for _ in range(trials):
        xs = [rng.randint(-5, 5) for _ in range(rng.randint(0, 8))]
        out = sort(xs[:])
        if out != sorted(out): return f"FAILS 'output is ordered' for {xs}"
        if sorted(xs) != sorted(out): return f"FAILS 'same elements as input' for {xs} -> {out}"
        if sort(out) != out: return f"FAILS 'idempotent' for {xs}"
    return "all properties held for 500 random inputs"
print("my_sort   :", check_sort_properties(my_sort))
print("buggy_sort:", check_sort_properties(buggy_sort))
