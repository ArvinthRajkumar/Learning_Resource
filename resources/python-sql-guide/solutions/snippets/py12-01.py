import timeit
n = 20_000
lst, st = list(range(n)), set(range(n))
t_list = timeit.timeit("n - 1 in lst", globals={"n": n, "lst": lst}, number=300)
t_set = timeit.timeit("n - 1 in st", globals={"n": n, "st": st}, number=300)
front_list = timeit.timeit("l.insert(0, 1); l.pop(0)", setup="l = list(range(50000))", number=2000)
front_deque = timeit.timeit("d.appendleft(1); d.popleft()", setup="from collections import deque; d = deque(range(50000))", number=2000)
print("membership: set is faster than list by more than 20x:", t_list / t_set > 20)
print("front operations: deque is faster than list by more than 20x:", front_list / front_deque > 20)
