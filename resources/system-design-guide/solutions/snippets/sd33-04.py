import re, math
from collections import defaultdict
STOP = {"the", "a", "an", "and", "of", "to", "is", "in", "for", "on", "with"}
def stem(t):
    if t.endswith("ies") and len(t) > 4: return t[:-3] + "y"
    if t.endswith("ing") and len(t) > 5:
        t = t[:-3]
        return t[:-1] if len(t) > 2 and t[-1] == t[-2] else t           # running -> runn -> run
    if t.endswith("s") and not t.endswith("ss") and len(t) > 3: return t[:-1]
    return t
def analyse(text):
    return [stem(t) for t in re.findall(r"[a-z0-9]+", text.lower()) if t not in STOP]
DOCS = {
    1: "Red running shoes for men",
    2: "Blue running shorts with pockets",
    3: "Red leather shoes, classic style",
    4: "Waterproof trail running shoes in red and blue",
    5: "Leather belt for men",
}
index, doc_len = defaultdict(dict), {}
for doc_id, text in DOCS.items():
    terms = analyse(text); doc_len[doc_id] = len(terms)
    for t in terms: index[t][doc_id] = index[t].get(doc_id, 0) + 1          # term -> {doc: term frequency}
def edit_distance(a, b):
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]
vocabulary = sorted(index)
for typo in ("shose", "leathr", "blu"):
    best = sorted((edit_distance(typo, t), t) for t in vocabulary)[:2]
    print(f"{typo!r} -> suggestions {[t for d, t in best if d <= 2]} (distances {[d for d, t in best]})")
