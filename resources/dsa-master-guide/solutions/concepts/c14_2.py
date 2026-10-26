from collections import deque

def bfs(graph, start):
    visited, order = {start}, []
    q = deque([start])
    while q:
        node = q.popleft()
        order.append(node)
        for nb in graph[node]:
            if nb not in visited:
                visited.add(nb)        # mark on enqueue
                q.append(nb)
    return order

def dfs(graph, node, visited=None, order=None):
    visited = set() if visited is None else visited
    order = [] if order is None else order
    visited.add(node)
    order.append(node)
    for nb in graph[node]:
        if nb not in visited:
            dfs(graph, nb, visited, order)
    return order
