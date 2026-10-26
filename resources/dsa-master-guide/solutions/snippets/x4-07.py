class Trie:
    def __init__(self): self.root = {}
    def insert(self, word):
        node = self.root
        for ch in word: node = node.setdefault(ch, {})
        node["$"] = True
    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node: return []
            node = node[ch]
        out = []
        def walk(n, acc):
            for k in sorted(n):
                if k == "$": out.append(acc)
                else: walk(n[k], acc + k)
        walk(node, prefix)
        return out
t = Trie()
for w in ["car", "card", "care", "cart", "cat", "dog"]: t.insert(w)
print(t.starts_with("car"), t.starts_with("ca"), t.starts_with("x"))
