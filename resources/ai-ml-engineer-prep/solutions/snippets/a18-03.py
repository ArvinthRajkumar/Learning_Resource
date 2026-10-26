actual    = [1] * 10 + [0] * 990                              # 1% of cases are positive
lazy      = [0] * 1000                                         # a model that always says "negative"
decent    = [1] * 7 + [0] * 3 + [1] * 20 + [0] * 970           # finds 7 of 10, raises 20 false alarms
def scores(pred):
    tp = sum(p and a for p, a in zip(pred, actual)); fp = sum(p and not a for p, a in zip(pred, actual)); fn = sum(a and not p for p, a in zip(pred, actual))
    acc = sum(p == a for p, a in zip(pred, actual)) / len(actual)
    return acc, tp / max(1, tp + fp), tp / max(1, tp + fn)
for name, pred in [("always 'no'", lazy), ("a real model", decent)]:
    a, p, r = scores(pred); print(f"{name:>12}: accuracy {a:.1%}, precision {p:.1%}, recall {r:.1%}")
