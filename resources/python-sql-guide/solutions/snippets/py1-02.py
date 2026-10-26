point = (3, 4)
x, y = point                      # unpacking
a, *middle, z = [1, 2, 3, 4, 5]   # star captures the rest
print(x, y, a, middle, z)
a, b = 1, 2
a, b = b, a                       # swap without a temporary
print(a, b)
