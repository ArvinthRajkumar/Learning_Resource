def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

def count_nodes(node):
    if node is None:
        return 0
    return 1 + count_nodes(node.left) + count_nodes(node.right)

def is_balanced(node):
    def check(n):                       # returns height or -1 if unbalanced
        if n is None:
            return 0
        l, r = check(n.left), check(n.right)
        if l == -1 or r == -1 or abs(l - r) > 1:
            return -1
        return 1 + max(l, r)
    return check(node) != -1
