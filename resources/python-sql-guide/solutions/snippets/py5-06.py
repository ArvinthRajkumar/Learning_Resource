import timeit
setup = "data = list(range(10000))"
t_list = timeit.timeit("9999 in data", setup, number=2000)
t_set = timeit.timeit("9999 in s", setup + "; s = set(data)", number=2000)
print("set is faster than list for membership:", t_set < t_list)
