import math
ratings = {"ann": {"A": 5, "B": 4, "C": 1}, "bob": {"A": 4, "B": 5, "D": 2},
           "cy": {"A": 1, "C": 5, "D": 4}, "dee": {"B": 5, "C": 2, "D": 1}}
def cosine(u, v):
    common = set(u) & set(v)
    if not common: return 0.0
    num = sum(u[i] * v[i] for i in common)
    return num / (math.sqrt(sum(x * x for x in u.values())) * math.sqrt(sum(x * x for x in v.values())))
target = "ann"
sims = {u: cosine(ratings[target], ratings[u]) for u in ratings if u != target}
print({u: round(s, 2) for u, s in sims.items()})
unseen = {"D"}
for item in unseen:
    num = sum(sims[u] * ratings[u][item] for u in sims if item in ratings[u])
    den = sum(abs(sims[u]) for u in sims if item in ratings[u])
    print("predicted rating of", item, "for", target, "=", round(num / den, 2))
