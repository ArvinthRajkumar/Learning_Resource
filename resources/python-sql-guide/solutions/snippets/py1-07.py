total = sum(n * n for n in range(1_000_000))
print(total)
print(any(n > 5 for n in [1, 9]), all(n > 0 for n in [1, 2, 0]))
