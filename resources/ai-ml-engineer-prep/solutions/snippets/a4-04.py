import math
sim = [[0.9, 0.2, 0.1],      # row i: similarity of query i to documents 0..2 (document i is the match)
       [0.3, 0.8, 0.2],
       [0.1, 0.4, 0.7]]
temp = 0.1
loss = 0
for i, row in enumerate(sim):
    logits = [s / temp for s in row]
    m = max(logits)
    lse = m + math.log(sum(math.exp(l - m) for l in logits))
    loss += -(logits[i] - lse)                # -log softmax at the correct document
print("InfoNCE loss: %.4f" % (loss / len(sim)))
