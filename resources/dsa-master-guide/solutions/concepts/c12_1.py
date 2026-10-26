def inorder(node, out):
    if node is None:
        return out
    inorder(node.left, out)       # 1. left subtree
    out.append(node.val)          # 2. this node
    inorder(node.right, out)      # 3. right subtree
    return out

def preorder(node, out):
    if node is None:
        return out
    out.append(node.val)
    preorder(node.left, out)
    preorder(node.right, out)
    return out

def postorder(node, out):
    if node is None:
        return out
    postorder(node.left, out)
    postorder(node.right, out)
    out.append(node.val)
    return out
