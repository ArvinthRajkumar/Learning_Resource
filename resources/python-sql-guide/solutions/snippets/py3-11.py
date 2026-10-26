import sys, gc, weakref
x = []
before = sys.getrefcount(x)
y = x                                  # one more reference
print(sys.getrefcount(x) - before)     # exactly one more

class Node:
    def __init__(self): self.other = None
a, b = Node(), Node()
a.other, b.other = b, a               # a reference cycle
r = weakref.ref(a)
del a, b
print(r() is not None)                # still alive (cycle)
gc.collect()
print(r() is None)                    # the cycle collector freed it
