import heapq
class Autocomplete:
    def __init__(self, sentences, times):
        self.root, self.cur, self.node = {}, "", None
        for s, t in zip(sentences, times): self._add(s, t)
        self.node = self.root
    def _add(self, s, t):
        node = self.root
        for ch in s:
            node = node.setdefault(ch, {})
            node.setdefault("#", {}); node["#"][s] = node["#"].get(s, 0) + t     # each prefix node stores sentence counts
    def input(self, ch):
        if ch == "#":
            self._add(self.cur, 1); self.cur, self.node = "", self.root; return []
        self.cur += ch
        if self.node is not None and ch in self.node: self.node = self.node[ch]
        else: self.node = None; return []
        return [s for s, _ in heapq.nsmallest(3, self.node["#"].items(), key=lambda kv: (-kv[1], kv[0]))]
ac = Autocomplete(["i love you", "island", "ironman", "i love leetcode"], [5, 3, 2, 2])
print([ac.input(c) for c in "i a"], ac.input("#"))
print("after typing 'i a#' once, the new sentence is remembered:", [ac.input(c) for c in "i a"][-1])
