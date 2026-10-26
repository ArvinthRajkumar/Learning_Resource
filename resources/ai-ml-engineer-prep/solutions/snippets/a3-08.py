import math
sig = lambda z: 1 / (1 + math.exp(-z))
def lstm_step(x, h, c, W):
    f = sig(W["f"][0] * x + W["f"][1] * h)       # forget gate
    i = sig(W["i"][0] * x + W["i"][1] * h)       # input gate
    g = math.tanh(W["g"][0] * x + W["g"][1] * h) # candidate
    o = sig(W["o"][0] * x + W["o"][1] * h)       # output gate
    c = f * c + i * g                            # additive cell update
    return o * math.tanh(c), c
W = {k: (0.5, 0.3) for k in "figo"}
h = c = 0.0
for x in (1.0, 0.0, 0.0, 0.0):
    h, c = lstm_step(x, h, c, W)
    print("h %.3f c %.3f" % (h, c))
