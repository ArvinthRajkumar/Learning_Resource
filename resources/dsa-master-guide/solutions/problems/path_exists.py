def path_exists(n, edges, source, destination):
    graph = [[] for _ in range(n)]
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
    seen, stack = {source}, [source]
    while stack:
        node = stack.pop()
        if node == destination:
            return True
        for nb in graph[node]:
            if nb not in seen:
                seen.add(nb)
                stack.append(nb)
    return False
