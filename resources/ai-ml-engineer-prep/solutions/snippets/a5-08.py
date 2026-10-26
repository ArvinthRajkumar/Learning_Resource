import random, math
random.seed(0)
weights = [random.gauss(0, 0.05) for _ in range(4096)]
weights[7] = 0.9                                       # one large outlier weight
def quant_error(vals, bits, group=None):
    qmax = 2 ** (bits - 1) - 1
    err = 0.0
    chunks = [vals] if group is None else [vals[i:i + group] for i in range(0, len(vals), group)]
    for c in chunks:
        s = max(abs(v) for v in c) / qmax
        err += sum((v - round(v / s) * s) ** 2 for v in c)
    return math.sqrt(err / len(vals))
for bits in (8, 6, 4):
    print("int%d: RMS error per-tensor %.5f | per-group-of-64 %.5f" % (bits, quant_error(weights, bits), quant_error(weights, bits, 64)))
