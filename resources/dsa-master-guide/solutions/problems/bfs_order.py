from collections import deque

def bfs_order(graph, start):
    visited = {start}
    order, q = [], deque([start])
    while q:
        node = q.popleft()
        order.append(node)
        for nb in graph[node]:
            if nb not in visited:
                visited.add(nb)
                q.append(nb)
    return order
