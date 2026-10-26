import random
random.seed(6)
class Node:
    __slots__ = ("key", "pri", "left", "right", "size")
    def __init__(self, key): self.key, self.pri, self.left, self.right, self.size = key, random.random(), None, None, 1
def sz(t): return t.size if t else 0
def upd(t): t.size = 1 + sz(t.left) + sz(t.right)
def split(t, key):                                                # (keys < key, keys >= key)
    if not t: return None, None
    if t.key < key:
        a, b = split(t.right, key); t.right = a; upd(t); return t, b
    a, b = split(t.left, key); t.left = b; upd(t); return a, t
def merge(a, b):                                                  # all keys of a < all keys of b
    if not a or not b: return a or b
    if a.pri > b.pri: a.right = merge(a.right, b); upd(a); return a
    b.left = merge(a, b.left); upd(b); return b
def insert(t, key):
    a, b = split(t, key); return merge(merge(a, Node(key)), b)
def erase(t, key):
    a, b = split(t, key); _, c = split(b, key + 1); return merge(a, c)
def kth(t, k):                                                    # k-th smallest, 0-indexed
    while t:
        if k < sz(t.left): t = t.left
        elif k == sz(t.left): return t.key
        else: k -= sz(t.left) + 1; t = t.right
def height(t): return 0 if not t else 1 + max(height(t.left), height(t.right))
root, shadow = None, []
for _ in range(2000):
    x = random.randrange(10_000)
    if x in shadow: continue
    shadow.append(x); root = insert(root, x)
for x in random.sample(shadow, 500):
    root = erase(root, x); shadow.remove(x)
shadow.sort()
assert all(kth(root, i) == shadow[i] for i in range(0, len(shadow), 17))
print(f"{sz(root)} keys after random inserts and deletes; order statistics verified; height {height(root)} (a balanced tree would be about {len(shadow).bit_length()}, a chain would be {len(shadow)})")
