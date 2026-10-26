class NestedIterator:
    def __init__(self, nested): self.stack, self.peeked = [iter(nested)], None
    def has_next(self):
        while self.peeked is None and self.stack:
            try: item = next(self.stack[-1])
            except StopIteration: self.stack.pop(); continue
            if isinstance(item, list): self.stack.append(iter(item))
            else: self.peeked = item
        return self.peeked is not None
    def next(self):
        if not self.has_next(): raise StopIteration
        v, self.peeked = self.peeked, None
        return v
it = NestedIterator([[1, [2, 3]], [], 4, [[5], [[6]]]])
out = []
while it.has_next(): out.append(it.next())
assert out == [1, 2, 3, 4, 5, 6]
print("flattened lazily, skipping the empty list:", out)
