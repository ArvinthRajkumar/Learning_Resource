from collections import deque

def right_side_view(root):
    if not root:
        return []
    res, q = [], deque([root])
    while q:
        for i in range(len(q)):
            node = q.popleft()
            last = node
            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
        res.append(last.val)          # last node processed in this level
    return res
