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
print("terms:", sorted(index))
print("postings for 'shoe':", dict(index["shoe"]), "| for 'red':", dict(index["red"]))
def search_and(query):
    postings = [set(index.get(t, {})) for t in analyse(query)]
    return sorted(set.intersection(*postings)) if postings else []
print("'red shoes' (AND):", search_and("red shoes"), "| 'running shoes red blue':", search_and("running shoes red blue"))
