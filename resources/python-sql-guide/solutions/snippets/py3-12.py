import sys
a, b = 256, 256
print(a is b)                         # small ints are cached
print([1, 2] == [1, 2], [1, 2] is [1, 2])
t = (1, [2, 3])
t[1].append(4)                        # a tuple's items are fixed, but a list inside can change
print(t)
print(sys.getsizeof([0] * 100) > sys.getsizeof([]))
