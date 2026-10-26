import random
random.seed(3)
concepts = {"cat": 5000, "sunset": 4000, "car": 2500, "lighthouse": 120, "abacus": 30}
total = sum(concepts.values())
print("natural share:", {k: f"{v / total:.1%}" for k, v in concepts.items()})
def balanced_weights(counts, temperature=0.5):                         # sample proportional to count ** temperature (1 = natural, 0 = uniform)
    w = {k: v ** temperature for k, v in counts.items()}; z = sum(w.values()); return {k: v / z for k, v in w.items()}
for temp in (1.0, 0.5, 0.0):
    print(f"temperature {temp}:", {k: f"{v:.1%}" for k, v in balanced_weights(concepts, temp).items()})
print("an image of an 'abacus' appears in about", f"{balanced_weights(concepts, 0.5)['abacus'] / (30 / total):.0f}x", "more batches than its natural frequency would give (so repeat epochs on rare images matter: watch for memorisation)")
