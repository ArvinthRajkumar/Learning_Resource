import random
random.seed(1)
true_w = 1.0
w, ema, decay = 0.0, 0.0, 0.999
errs_w, errs_ema = [], []
for step in range(20000):
    g = 2 * (w - true_w) + random.gauss(0, 3)      # noisy gradient of (w - true)^2
    w -= 0.02 * g
    ema = decay * ema + (1 - decay) * w
    if step > 5000:
        errs_w.append(abs(w - true_w)); errs_ema.append(abs(ema - true_w))
print("mean error of raw weight : %.3f" % (sum(errs_w) / len(errs_w)))
print("mean error of EMA weight : %.3f" % (sum(errs_ema) / len(errs_ema)))
