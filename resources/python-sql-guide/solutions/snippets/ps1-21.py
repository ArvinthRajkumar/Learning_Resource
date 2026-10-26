t = (1, [2])
t[1].append(3)
print(t)
try:
    t[0] = 9
except TypeError:
    print("immutable")
