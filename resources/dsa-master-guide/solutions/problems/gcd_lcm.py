def gcd_lcm(a, b):
    x, y = a, b
    while y:
        x, y = y, x % y     # Euclid
    return x, a // x * b
