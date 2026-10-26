import random
random.seed(5)

class Node:
    def __init__(self, key):
        self.key, self.left, self.right, self.h = key, None, None, 1
h = lambda n: n.h if n else 0
def upd(n): n.h = 1 + max(h(n.left), h(n.right))
def balance(n): return h(n.left) - h(n.right)
def rot_right(y):
    x = y.left; y.left, x.right = x.right, y
    upd(y); upd(x); return x
def rot_left(x):
    y = x.right; x.right, y.left = y.left, x
    upd(x); upd(y); return y
def insert(n, key):
    if not n: return Node(key)
    if key < n.key: n.left = insert(n.left, key)
    elif key > n.key: n.right = insert(n.right, key)
    else: return n
    upd(n)
    b = balance(n)
    if b > 1 and key < n.left.key: return rot_right(n)
    if b < -1 and key > n.right.key: return rot_left(n)
    if b > 1: n.left = rot_left(n.left); return rot_right(n)
    if b < -1: n.right = rot_right(n.right); return rot_left(n)
    return n
def inorder(n): return inorder(n.left) + [n.key] + inorder(n.right) if n else []
def valid(n):
    return True if not n else abs(balance(n)) <= 1 and valid(n.left) and valid(n.right)

root = None
for k in range(1, 1025):                    # sorted insertion: the worst case for a plain BST
    root = insert(root, k)
print("height after inserting 1..1024 in order:", root.h, "(a plain BST would be 1024)")
root2 = None
keys = random.sample(range(10000), 500)
for k in keys: root2 = insert(root2, k)
print("random keys sorted correctly:", inorder(root2) == sorted(keys), "| balanced everywhere:", valid(root2), "| height", root2.h)
