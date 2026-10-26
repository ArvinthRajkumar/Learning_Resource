# Gradient boosting with stumps on a 1D regression problem.
xs = [i / 5 for i in range(50)]
ys = [x * x / 10 for x in xs]                    # a curve; a linear model cannot fit it
def best_stump(res):
    best = None
    for thr in [x + 0.1 for x in xs]:
        l = [r for x, r in zip(xs, res) if x <= thr]; rr = [r for x, r in zip(xs, res) if x > thr]
        if not l or not rr: continue
        lm, rm = sum(l) / len(l), sum(rr) / len(rr)
        err = sum((r - (lm if x <= thr else rm)) ** 2 for x, r in zip(xs, res))
        if best is None or err < best[0]: best = (err, thr, lm, rm)
    return best
pred, lr = [0.0] * len(xs), 0.3
for m in range(40):
    res = [y - p for y, p in zip(ys, pred)]
    _, thr, lm, rm = best_stump(res)
    pred = [p + lr * (lm if x <= thr else rm) for p, x in zip(pred, xs)]
    if m in (0, 9, 39):
        print("after %2d stumps: MSE %.3f" % (m + 1, sum((y - p) ** 2 for y, p in zip(ys, pred)) / len(ys)))
