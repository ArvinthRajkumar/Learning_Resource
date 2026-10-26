import math, random
random.seed(5)
logits = {"cat": 3.0, "dog": 2.5, "pizza": 0.5, "the": -1.0}
def sample(temp):
    scaled = {w: v / temp for w, v in logits.items()}; m = max(scaled.values())
    exp = {w: math.exp(v - m) for w, v in scaled.items()}; s = sum(exp.values())
    probs = {w: e / s for w, e in exp.items()}
    return probs, random.choices(list(probs), weights=list(probs.values()))[0]
for t in (0.2, 1.0, 2.0):
    probs, pick = sample(t); print(f"temperature {t}: probabilities {({w: round(p, 2) for w, p in probs.items()})}")
