def build_tree_pre_in(preorder, inorder):
    index = {v: i for i, v in enumerate(inorder)}
    pos = 0
    def build(lo, hi):
        nonlocal pos
        if lo > hi:
            return None
        val = preorder[pos]
        pos += 1
        node = TreeNode(val)
        mid = index[val]
        node.left = build(lo, mid - 1)
        node.right = build(mid + 1, hi)
        return node
    return build(0, len(inorder) - 1)

def level_values(root):
    out, q = [], [root] if root else []
    while q:
        n = q.pop(0)
        out.append(n.val)
        q += [c for c in (n.left, n.right) if c]
    return out
