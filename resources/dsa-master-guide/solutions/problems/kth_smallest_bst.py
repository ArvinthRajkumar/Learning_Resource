def kth_smallest_bst(root, k):
    stack, node = [], root
    while stack or node:
        while node:                  # go as far left as possible
            stack.append(node)
            node = node.left
        node = stack.pop()
        k -= 1
        if k == 0:
            return node.val
        node = node.right
