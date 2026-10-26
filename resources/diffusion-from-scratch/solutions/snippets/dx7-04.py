import math
def clip(grads, max_norm):
    norm = math.sqrt(sum(g * g for g in grads))
    scale = min(1.0, max_norm / (norm + 1e-6))
    return [g * scale for g in grads], norm
g, n = clip([30.0, 40.0], 1.0)
print("norm was", n, "-> clipped gradient", [round(x, 3) for x in g])
