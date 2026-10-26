def lca(root, p, q):
    def go(node):
        if node is None or node.val in (p, q):
            return node
        left, right = go(node.left), go(node.right)
        if left and right:
            return node            # p and q are on different sides
        return left or right
    return go(root).val
