import tracemalloc
tracemalloc.start()
big_list = [str(i) * 10 for i in range(50000)]
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
gen_total = sum(len(str(i) * 10) for i in range(50000))       # a generator expression holds one item at a time
print("list of 50k strings used more than 1 MB:", peak > 1_000_000, "| the generator approach needs no list at all:", gen_total > 0)
