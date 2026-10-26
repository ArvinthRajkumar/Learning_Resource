class WordDictionary:
    def __init__(self):
        self.root = {}

    def add_word(self, word):
        node = self.root
        for ch in word:
            node = node.setdefault(ch, {})
        node["$"] = True

    def search(self, word):
        def go(node, i):
            if i == len(word):
                return "$" in node
            ch = word[i]
            if ch == ".":
                return any(go(child, i + 1) for key, child in node.items() if key != "$")
            return ch in node and go(node[ch], i + 1)
        return go(self.root, 0)
