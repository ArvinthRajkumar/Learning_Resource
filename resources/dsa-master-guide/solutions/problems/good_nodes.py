def good_nodes(root):
    def go(node, best):
        if not node:
            return 0
        good = 1 if node.val >= best else 0
        best = max(best, node.val)
        return good + go(node.left, best) + go(node.right, best)
    return go(root, float("-inf"))
