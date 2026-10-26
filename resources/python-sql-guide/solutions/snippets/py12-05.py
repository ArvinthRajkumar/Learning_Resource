def numbers():
    n = 0
    while True: yield n; n += 1
def take(it, k): return [next(it) for _ in range(k)]
squares = (x * x for x in numbers())
print(take(squares, 5), "| continues:", take(squares, 3))
gen = (x for x in range(3))
print(list(gen), list(gen), "(the second pass is empty: a generator is exhausted once consumed)")
print("sum of squares below one million, streamed:", sum(x * x for x in range(1_000_000)))
