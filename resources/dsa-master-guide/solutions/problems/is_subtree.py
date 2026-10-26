def is_subtree(root, sub):
    def same(a, b):
        if not a and not b:
            return True
        if not a or not b or a.val != b.val:
            return False
        return same(a.left, b.left) and same(a.right, b.right)
    if not root:
        return sub is None
    return same(root, sub) or is_subtree(root.left, sub) or is_subtree(root.right, sub)
