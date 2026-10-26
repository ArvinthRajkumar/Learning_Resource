class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})   # create the child if missing
        node["$"] = True                     # end-of-word marker

    def _find(self, text):
        node = self.root
        for ch in text:
            if ch not in node:
                return None
            node = node[ch]
        return node

    def search(self, word):
        node = self._find(word)
        return node is not None and "$" in node

    def starts_with(self, prefix):
        return self._find(prefix) is not None
