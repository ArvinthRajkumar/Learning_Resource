import math
def schedule(step, total, warmup, peak=1.0, floor=0.1):
    if step < warmup:
        return peak * step / warmup                      # linear warm-up
    progress = (step - warmup) / max(1, total - warmup)
    return floor * peak + (peak - floor * peak) * 0.5 * (1 + math.cos(math.pi * progress))   # cosine decay
for s in (0, 50, 100, 500, 900, 1000):
    print("step %4d lr %.3f" % (s, schedule(s, 1000, 100)))
