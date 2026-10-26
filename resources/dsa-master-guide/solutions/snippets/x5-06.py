def crt(rems, mods):
    x, M = 0, 1
    for r, m in zip(rems, mods):
        # solve x + M*t = r (mod m)
        t = ((r - x) * pow(M, -1, m)) % m
        x += M * t
        M *= m
    return x % M, M
x, M = crt([2, 3, 2], [3, 5, 7])
print("x =", x, "mod", M, "| check:", x % 3, x % 5, x % 7)
