a = [1, [2, 3]]
b = a                   # same object
c = a.copy()            # shallow copy: new outer list, same inner list
import copy
d = copy.deepcopy(a)    # fully independent
a[1].append(4)
print(b, c, d)
print(a is b, a is c, a == c)
