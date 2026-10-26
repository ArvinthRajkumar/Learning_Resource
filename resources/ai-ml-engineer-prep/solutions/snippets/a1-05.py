import math
spam = ["win money now", "free money offer", "win a free prize"]
ham = ["meeting at noon", "project status update", "lunch at noon tomorrow"]
def counts(docs):
    c = {}
    for d in docs:
        for w in d.split():
            c[w] = c.get(w, 0) + 1
    return c
cs, ch = counts(spam), counts(ham)
vocab = set(cs) | set(ch)
def score(msg, c, prior):
    total = sum(c.values())
    return math.log(prior) + sum(math.log((c.get(w, 0) + 1) / (total + len(vocab))) for w in msg.split() if w in vocab)
for msg in ("free money", "status at noon"):
    s_spam, s_ham = score(msg, cs, 0.5), score(msg, ch, 0.5)
    print(msg, "->", "spam" if s_spam > s_ham else "ham")
