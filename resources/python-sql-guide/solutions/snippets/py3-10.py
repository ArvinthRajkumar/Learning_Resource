import functools, itertools, operator
print(functools.reduce(operator.mul, [1, 2, 3, 4]))
add5 = functools.partial(operator.add, 5)
print(add5(10))
print(list(itertools.chain([1, 2], [3])), list(itertools.accumulate([1, 2, 3, 4])))
print(list(itertools.combinations("abc", 2)), list(itertools.product([0, 1], repeat=2)))
print(list(itertools.permutations([1, 2, 3], 2))[:3])
data = sorted(["apple", "avocado", "banana", "blueberry", "cherry"], key=lambda w: w[0])
for k, grp in itertools.groupby(data, key=lambda w: w[0]):
    print(k, list(grp))
print(list(itertools.islice(itertools.cycle("ab"), 5)), list(itertools.zip_longest([1, 2, 3], "a", fillvalue="-")))
