import random
random.seed(5)
tokens = "diffusion models can also generate text".split()
def mask(tokens, p):
    return [t if random.random() > p else "[M]" for t in tokens]
for p in (0.0, 0.3, 0.7, 1.0):
    print("mask prob %.1f ->" % p, " ".join(mask(tokens, p)))
