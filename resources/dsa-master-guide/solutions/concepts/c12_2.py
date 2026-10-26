def bst_search(node, target):
    while node:
        if target == node.val:
            return True
        node = node.left if target < node.val else node.right
    return False

def bst_insert(node, val):
    if node is None:
        return TreeNode(val)           # found the empty spot
    if val < node.val:
        node.left = bst_insert(node.left, val)
    elif val > node.val:
        node.right = bst_insert(node.right, val)
    return node
