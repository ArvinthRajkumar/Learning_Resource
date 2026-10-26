import math
def softmax(xs):
    m = max(xs); e = [math.exp(x - m) for x in xs]; s = sum(e)
    return [x / s for x in e]
router_scores = [0.1, 2.0, -0.5, 1.5, 0.0, -1.0, 0.7, 0.2]   # logits for 8 experts for one token
k = 2
top = sorted(range(8), key=lambda i: -router_scores[i])[:k]
gates = softmax([router_scores[i] for i in top])
print("chosen experts:", top, "gate weights:", [round(g, 3) for g in gates])
# parameter accounting for an 8-expert, top-2 model
dense_ffn, experts, shared = 100, 8, 400                       # arbitrary units of parameters
print("total params:", shared + experts * dense_ffn, " active per token:", shared + k * dense_ffn)
