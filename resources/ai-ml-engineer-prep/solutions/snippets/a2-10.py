import math
# Minimise f(x, y) = x^2 + 10 y^2 (a narrow valley) with plain GD, momentum and Adam.
grad = lambda x, y: (2 * x, 20 * y)
def run(update, steps=60):
    x, y, state = 1.0, 1.0, {}
    for t in range(1, steps + 1):
        gx, gy = grad(x, y)
        x, y = update(x, y, gx, gy, state, t)
    return x * x + 10 * y * y
def gd(x, y, gx, gy, s, t, lr=0.05): return x - lr * gx, y - lr * gy
def momentum(x, y, gx, gy, s, t, lr=0.05, b=0.9):
    vx, vy = s.get("v", (0, 0)); vx, vy = b * vx + gx, b * vy + gy; s["v"] = (vx, vy)
    return x - lr * vx, y - lr * vy
def adam(x, y, gx, gy, s, t, lr=0.1, b1=0.9, b2=0.999):
    m = s.get("m", (0, 0)); v = s.get("v", (0, 0))
    m = (b1 * m[0] + (1 - b1) * gx, b1 * m[1] + (1 - b1) * gy)
    v = (b2 * v[0] + (1 - b2) * gx * gx, b2 * v[1] + (1 - b2) * gy * gy)
    s["m"], s["v"] = m, v
    mh = (m[0] / (1 - b1 ** t), m[1] / (1 - b1 ** t)); vh = (v[0] / (1 - b2 ** t), v[1] / (1 - b2 ** t))
    return x - lr * mh[0] / (math.sqrt(vh[0]) + 1e-8), y - lr * mh[1] / (math.sqrt(vh[1]) + 1e-8)
for name, u in (("gradient descent", gd), ("momentum", momentum), ("adam", adam)):
    print("%-16s final loss %.6f" % (name, run(u)))
