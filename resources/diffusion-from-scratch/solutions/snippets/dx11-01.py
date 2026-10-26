import math, random
random.seed(1)
pixel = 0.8                                                     # one pixel of a clean image, scaled to [-1, 1]
T = 10
betas = [0.05 + 0.1 * i / (T - 1) for i in range(T)]            # a small noise schedule
alpha_bar = 1.0; rows = []
for t, b in enumerate(betas, 1):
    alpha_bar *= (1 - b)
    signal, noise = math.sqrt(alpha_bar), math.sqrt(1 - alpha_bar)
    rows.append((t, signal, noise))
for t, s, n in rows[::3]:
    print(f"step {t:>2}: keep {s:.2f} of the signal and mix in {n:.2f} of noise  -> pixel value about {s * pixel:.2f} + {n:.2f} x random")
