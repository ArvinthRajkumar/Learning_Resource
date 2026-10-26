import timeit
lst = list(range(100_000)); st = set(lst)
t_list = timeit.timeit("99_999 in lst", globals={"lst": lst}, number=200)
t_set = timeit.timeit("99_999 in st", globals={"st": st}, number=200)
print("set lookup beats list scan by more than 50x:", t_list / t_set > 50)
d = {}
for k in ["b", "a", "c"]: d[k] = 1
print("dict preserves insertion order:", list(d), "| mutable keys are rejected:", end=" ")
try: {[1]: 2}
except TypeError as e: print(e)
