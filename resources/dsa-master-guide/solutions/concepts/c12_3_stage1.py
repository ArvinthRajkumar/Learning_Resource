def height(n):
    return 0 if not n else 1 + max(height(n.left), height(n.right))

def is_balanced(root):
    if not root:
        return True
    return (abs(height(root.left) - height(root.right)) <= 1 and
            is_balanced(root.left) and is_balanced(root.right))
