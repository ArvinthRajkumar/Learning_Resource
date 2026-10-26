import math
docs = ["the cat sat on the mat", "the dog sat on the log", "cats and dogs are pets"]
tokens = [d.split() for d in docs]
N = len(docs)
vocab = sorted({w for t in tokens for w in t})
df = {w: sum(w in t for t in tokens) for w in vocab}
def tfidf(t):
    return {w: (t.count(w) / len(t)) * math.log(N / df[w]) for w in sorted(set(t))}
for d, t in zip(docs, tokens):
    top = sorted(tfidf(t).items(), key=lambda kv: (-round(kv[1], 6), kv[0]))[:3]
    print(d, "->", [(w, round(s, 2)) for w, s in top])
