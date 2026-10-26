import math, random
random.seed(7)
def softmax(z):
    m = max(z); e = [math.exp(v - m) for v in z]; s = sum(e); return [v / s for v in e]
def sample(n, overconfidence):
    out = []
    for _ in range(n):
        label = random.randrange(3); logits = [random.gauss(0, 1) for _ in range(3)]; logits[label] += 1.0     # weak true signal
        out.append(([overconfidence * l for l in logits], label))
    return out
def ece(items, T=1.0, bins=10):
    buckets = [[] for _ in range(bins)]
    for logits, label in items:
        p = softmax([l / T for l in logits]); conf = max(p); buckets[min(bins - 1, int(conf * bins))].append((conf, p.index(conf) == label))
    return sum(len(b) / len(items) * abs(sum(c for c, _ in b) / len(b) - sum(ok for _, ok in b) / len(b)) for b in buckets if b)
items = sample(6000, overconfidence=3.0)                          # scaled-up logits mimic an over-confident network
best_T = min((t / 10 for t in range(5, 80)), key=lambda T: ece(items[:3000], T))
print(f"ECE before temperature scaling {ece(items[3000:]):.3f} | learned T = {best_T:.1f} | ECE after {ece(items[3000:], best_T):.3f}")
