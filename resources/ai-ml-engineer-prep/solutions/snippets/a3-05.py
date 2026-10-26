import random
random.seed(2)
p = 0.5
acts = [1.0] * 10
mask_scaled = [a / (1 - p) if random.random() > p else 0.0 for a in acts]
print(mask_scaled, "mean %.2f (expected 1.0 on average)" % (sum(mask_scaled) / 10))
avg = sum(sum(a / (1 - p) if random.random() > p else 0.0 for a in acts) / 10 for _ in range(2000)) / 2000
print("average over many masks: %.3f" % avg)
