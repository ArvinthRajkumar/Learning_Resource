def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

from itertools import islice
print(list(islice(fib(), 10)))

def read_chunks(items, size):
    for i in range(0, len(items), size):
        yield items[i:i + size]
print(list(read_chunks(list(range(7)), 3)))
