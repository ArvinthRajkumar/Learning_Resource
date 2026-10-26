def invert_tree(root):
    if root is None:
        return None
    root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root

def level_values(root):
    out, q = [], [root] if root else []
    while q:
        node = q.pop(0)
        out.append(node.val)
        q += [c for c in (node.left, node.right) if c]
    return out
