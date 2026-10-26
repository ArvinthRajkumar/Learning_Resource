import math
def psi(ref, cur):
    return sum((c - r) * math.log(c / r) for r, c in zip(ref, cur))
ref = [0.25, 0.25, 0.25, 0.25]            # share of training data in 4 quartile bins
stable = [0.24, 0.26, 0.26, 0.24]
shifted = [0.10, 0.20, 0.30, 0.40]
print("PSI stable  :", round(psi(ref, stable), 4))
print("PSI shifted :", round(psi(ref, shifted), 4))
