import math, random
random.seed(0)
def gcd(a, b):
    while b: a, b = b, a % b
    return a
def ext_gcd(a, b):
    if b == 0: return a, 1, 0
    g, x, y = ext_gcd(b, a % b)
    return g, y, x - (a // b) * y
for _ in range(500):
    a, b = random.randint(1, 10**6), random.randint(1, 10**6)
    assert gcd(a, b) == math.gcd(a, b)
    g, x, y = ext_gcd(a, b)
    assert a * x + b * y == g
print("gcd and Bezout identity verified; ext_gcd(240, 46) =", ext_gcd(240, 46))
