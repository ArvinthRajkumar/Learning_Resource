def inorder(root):
    res = []
    def walk(node):
        if node:
            walk(node.left)
            res.append(node.val)
            walk(node.right)
    walk(root)
    return res
