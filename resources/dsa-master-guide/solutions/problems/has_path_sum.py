def has_path_sum(root, target):
    if root is None:
        return False
    if root.left is None and root.right is None:    # leaf
        return target == root.val
    rest = target - root.val
    return has_path_sum(root.left, rest) or has_path_sum(root.right, rest)
