# Solve dx/dt = -x from t=0 to 1 (exact answer exp(-1)) with Euler and Heun.
import math
def euler(n):
    x, h = 1.0, 1.0 / n
    for _ in range(n): x += h * (-x)
    return x
def heun(n):
    x, h = 1.0, 1.0 / n
    for _ in range(n):
        k1 = -x
        k2 = -(x + h * k1)
        x += h * (k1 + k2) / 2
    return x
exact = math.exp(-1)
for n in (4, 8, 16):
    print("steps %2d  euler error %.5f  heun error %.6f" % (n, abs(euler(n) - exact), abs(heun(n) - exact)))
