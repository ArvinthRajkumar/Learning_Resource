import math
def clip_loss(sim, temp=0.07):
    n = len(sim)
    total = 0.0
    for i in range(n):                                           # image to text
        row = [s / temp for s in sim[i]]
        m = max(row); lse = m + math.log(sum(math.exp(v - m) for v in row))
        total += lse - row[i]
    for j in range(n):                                           # text to image
        col = [sim[i][j] / temp for i in range(n)]
        m = max(col); lse = m + math.log(sum(math.exp(v - m) for v in col))
        total += lse - col[j]
    return total / (2 * n)
good = [[0.9, 0.1, 0.0], [0.1, 0.8, 0.2], [0.0, 0.2, 0.7]]
bad = [[0.3, 0.3, 0.3], [0.3, 0.3, 0.3], [0.3, 0.3, 0.3]]
print("matched model loss %.3f | uninformative model loss %.3f (ln 3 = %.3f)" % (clip_loss(good), clip_loss(bad), math.log(3)))
