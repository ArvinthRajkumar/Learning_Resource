from itertools import islice
from collections import deque

def chunked(iterable, n):
    it = iter(iterable)
    while chunk := list(islice(it, n)):
        yield chunk

def windows(iterable, n):
    it = iter(iterable)
    win = deque(islice(it, n), maxlen=n)
    if len(win) == n:
        yield tuple(win)
    for x in it:
        win.append(x)
        yield tuple(win)

print(list(chunked(range(7), 3)))
print(list(windows([1, 2, 3, 4, 5], 3)))
