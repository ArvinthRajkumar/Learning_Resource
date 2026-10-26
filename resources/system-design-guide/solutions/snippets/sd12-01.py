import re
docs = {
    1: "cache the database reads",
    2: "database replication and sharding",
    3: "a queue decouples workers",
    4: "queue and cache for speed",
    7: "database cache design",
}
index = {}
for doc_id, text in docs.items():
    for term in set(re.findall(r"[a-z]+", text.lower())):
        index.setdefault(term, []).append(doc_id)
for t in index:
    index[t].sort()

def search_and(*terms):
    sets = [set(index.get(t, [])) for t in terms]
    return sorted(set.intersection(*sets))

print(index["cache"], index["database"])
print(search_and("cache", "database"))
