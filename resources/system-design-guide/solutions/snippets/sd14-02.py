import heapq
class Trie:
    def __init__(self, k=3):
        self.k, self.root = k, {}
    def add(self, query, count):
        node = self.root
        for ch in query:
            node = node.setdefault(ch, {})
            top = node.setdefault("#", [])
            top.append((count, query))
            top.sort(reverse=True)
            del top[self.k:]
    def suggest(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node: return []
            node = node[ch]
        return [q for c, q in node.get("#", [])]

t = Trie()
for q, c in [("system design", 90), ("system", 60), ("sql join", 80), ("sql index", 40), ("syntax", 10)]:
    t.add(q, c)
print(t.suggest("sy"), t.suggest("sql"), t.suggest("z"))
