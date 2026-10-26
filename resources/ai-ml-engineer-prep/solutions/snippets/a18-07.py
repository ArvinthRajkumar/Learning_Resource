weights = [0.113, -0.482, 0.907, -0.031, 0.356, -0.774]
def quantize(ws, bits):
    levels = 2 ** (bits - 1) - 1; scale = max(abs(w) for w in ws) / levels
    return [round(w / scale) * scale for w in ws]
for bits in (8, 4, 2):
    q = quantize(weights, bits); err = max(abs(a - b) for a, b in zip(weights, q))
    print(f"{bits} bits ({2 ** bits} levels): max rounding error {err:.3f}")
