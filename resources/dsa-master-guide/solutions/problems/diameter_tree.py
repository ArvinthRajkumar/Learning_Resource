def diameter_tree(root):
    best = 0
    def height(node):
        nonlocal best
        if node is None:
            return 0
        l, r = height(node.left), height(node.right)
        best = max(best, l + r)          # path through this node
        return 1 + max(l, r)
    height(root)
    return best
