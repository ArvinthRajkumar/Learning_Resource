import sys, gc, weakref
x = object()
print("refcount after creating, one name plus the call argument:", sys.getrefcount(x))
y = x
print("after a second name:", sys.getrefcount(x))
del y
class Node:
    def __init__(self): self.other = None
a, b = Node(), Node()
a.other, b.other = b, a                     # a reference cycle
ref = weakref.ref(a)
del a, b
print("alive after del (cycle keeps it):", ref() is not None)
gc.collect()
print("alive after gc.collect():", ref() is not None)
