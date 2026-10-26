import random
random.seed(9)
class T:
    def __init__(self, v, l=None, r=None): self.v, self.l, self.r = v, l, r
def insert(t, v):
    if not t: return T(v)
    if v < t.v: t.l = insert(t.l, v)
    else: t.r = insert(t.r, v)
    return t
def is_bst(t, lo=float("-inf"), hi=float("inf")):
    return t is None or (lo < t.v < hi and is_bst(t.l, lo, t.v) and is_bst(t.r, t.v, hi))
def inorder(t): return inorder(t.l) + [t.v] + inorder(t.r) if t else []
vals = random.sample(range(100), 20)
root = None
for v in vals: root = insert(root, v)
assert is_bst(root) and inorder(root) == sorted(vals)
bad = T(5, T(1), T(4, T(3), T(6)))
print("valid BST:", is_bst(root), "| invalid tree detected:", not is_bst(bad), "| 5th smallest:", inorder(root)[4] == sorted(vals)[4])
