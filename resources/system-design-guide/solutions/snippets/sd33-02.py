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
def bm25_search(query, k1=1.2, b=0.75, top=5):
    N = len(DOCS); avg = sum(doc_len.values()) / N
    scores = defaultdict(float)
    for t in analyse(query):
        df = len(index.get(t, {}))
        if df == 0: continue
        idf = math.log(1 + (N - df + 0.5) / (df + 0.5))
        for d, tf in index[t].items():
            scores[d] += idf * tf * (k1 + 1) / (tf + k1 * (1 - b + b * doc_len[d] / avg))
    return sorted(((round(s, 3), d, DOCS[d]) for d, s in scores.items()), reverse=True)[:top]
for q in ("red shoes", "running"):
    print(f"query {q!r}:")
    for row in bm25_search(q): print("   ", row)
