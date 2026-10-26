import math
comps = [(-2.0, 0.3, 0.5), (2.5, 0.4, 0.5)]
def velocity(x, t):
    ws, vs = [], []
    for m, s, w in comps:
        var = (1 - t) ** 2 + t * t * s * s
        ws.append(w * math.exp(-0.5 * (x - t * m) ** 2 / var) / math.sqrt(var))
        vs.append((m + t * s * s / var * (x - t * m)) - (1 - t) * (x - t * m) / var)
    z = sum(ws); return sum(w * v for w, v in zip(ws, vs)) / z
def integrate(x, t0, t1, steps=2000):                      # fine Euler integration of the ODE along the flow
    dt = (t1 - t0) / steps
    for i in range(steps): x += velocity(x, t0 + i * dt) * dt
    return x
def consistency(x, t): return integrate(x, t, 0.999)       # where the trajectory through (x, t) ends up
x_start = 0.7
points = [(x_start, 0.0)]
for t in (0.2, 0.4, 0.6):                                   # walk along the trajectory, then ask the consistency function from each point
    points.append((integrate(x_start, 0.0, t), t))
print("points on one trajectory:", [(round(x, 2), t) for x, t in points])
print("consistency function output at each point:", [round(consistency(x, t), 2) for x, t in points], "(the same endpoint, up to integration error)")
