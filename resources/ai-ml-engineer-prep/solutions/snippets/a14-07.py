import random, math
random.seed(5)
def make_model(seed):                                          # a tiny "model": a random-sample polynomial fit (a stand-in for a network)
    rng = random.Random(seed); xs = [rng.uniform(-3, 3) for _ in range(25)]; ys = [math.sin(x) + rng.gauss(0, 0.2) for x in xs]
    def predict(x):                                            # kernel-weighted average of this model's own training sample
        w = [math.exp(-0.5 * ((x - xi) / 0.6) ** 2) + 1e-12 for xi in xs]; return sum(wi * yi for wi, yi in zip(w, ys)) / sum(w)
    return predict
ensemble = [make_model(s) for s in range(12)]
for x in (0.0, 2.0, 6.0, 10.0):
    preds = [m(x) for m in ensemble]; mean = sum(preds) / len(preds); sd = (sum((p - mean) ** 2 for p in preds) / len(preds)) ** 0.5
    print(f"x = {x:>4}: ensemble mean {mean:+.2f}, disagreement (std) {sd:.3f}" + ("   <- far outside the training range" if x > 4 else ""))
