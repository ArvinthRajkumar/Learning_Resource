import timeit
n = 200_000
data = list(range(n))
loop = timeit.timeit(lambda: [x * 2 + 1 for x in data], number=5)
builtin = timeit.timeit(lambda: sum(data), number=5)
print("a Python-level loop over 200k items is more costly than one built-in aggregation:", loop > builtin)
row_by_row = timeit.timeit("res = []\nfor i in range(20000): res = res + [i]", number=1)
collect = timeit.timeit("res = []\nfor i in range(20000): res.append(i)", number=1)
print("building a list by repeated concatenation is slower than append:", row_by_row > collect)
