from collections import deque

def is_bipartite(graph):
    color = {}
    for start in range(len(graph)):
        if start in color:
            continue
        color[start] = 0
        q = deque([start])
        while q:
            u = q.popleft()
            for v in graph[u]:
                if v not in color:
                    color[v] = 1 - color[u]      # opposite colour
                    q.append(v)
                elif color[v] == color[u]:
                    return False
    return True
