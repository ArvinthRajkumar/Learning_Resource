from collections import deque

def level_order(root):
    res, q = [], deque([root] if root else [])
    while q:
        res.append([n.val for n in q])
        for _ in range(len(q)):
            n = q.popleft()
            if n.left: q.append(n.left)
            if n.right: q.append(n.right)
    return res
