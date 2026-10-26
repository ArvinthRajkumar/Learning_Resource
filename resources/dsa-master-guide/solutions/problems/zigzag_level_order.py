from collections import deque

def zigzag_level_order(root):
    if not root:
        return []
    res, q, left_to_right = [], deque([root]), True
    while q:
        level = [q.popleft() for _ in range(len(q))]
        vals = [n.val for n in level]
        res.append(vals if left_to_right else vals[::-1])
        for n in level:
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
        left_to_right = not left_to_right
    return res
