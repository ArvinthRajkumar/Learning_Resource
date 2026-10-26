import math
# Tiny cross-attention with 3 words and 2 pixels, d = 2
text = {"red": [1.0, 0.0], "ball": [0.5, 0.5], "table": [0.0, 1.0]}
words = list(text)
K = [text[w] for w in words]
V = K
pixels = {"pixel on ball": [1.0, 0.2], "pixel on table": [0.0, 1.0]}
def softmax(xs):
    m = max(xs); e = [math.exp(x - m) for x in xs]; s = sum(e); return [x / s for x in e]
for name, q in pixels.items():
    scores = [sum(a * b for a, b in zip(q, k)) / math.sqrt(2) for k in K]
    w = softmax(scores)
    print(name, dict(zip(words, [round(x, 2) for x in w])))
