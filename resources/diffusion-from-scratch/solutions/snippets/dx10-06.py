# loss per timestep bucket tells you where the model is weak: early diffusion times are easy, high-noise times are hard
import random
random.seed(4)
buckets = ["t 0-100", "t 100-300", "t 300-600", "t 600-1000"]
base = [0.002, 0.010, 0.040, 0.120]                             # a typical shape of per-timestep MSE: small at low noise, larger at high noise
logged = [[b * random.uniform(0.8, 1.2) for _ in range(50)] for b in base]
for name, vals in zip(buckets, logged): print(f"{name:>11}: mean loss {sum(vals) / len(vals):.4f}")
print("a single averaged training loss would hide that the high-noise buckets, where global structure forms, are the ones that matter; log losses per bucket")
