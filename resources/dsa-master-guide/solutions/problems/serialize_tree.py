def serialize_tree(root):
    out = []
    def go(n):
        if not n:
            out.append("#")
            return
        out.append(str(n.val))
        go(n.left)
        go(n.right)
    go(root)
    return ",".join(out)

def deserialize_tree(data):
    it = iter(data.split(","))
    def go():
        tok = next(it)
        if tok == "#":
            return None
        node = TreeNode(int(tok))
        node.left = go()
        node.right = go()
        return node
    return go()
