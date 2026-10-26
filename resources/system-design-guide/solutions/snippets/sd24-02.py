import heapq
graph = {                     # node -> [(neighbour, minutes)]
    "A": [("B", 4), ("C", 2)], "B": [("D", 5)], "C": [("B", 1), ("D", 8), ("E", 10)],
    "D": [("F", 2)], "E": [("F", 3)], "F": [],
}
def dijkstra(src, dst, g):
    dist, prev, heap, pops = {src: 0}, {}, [(0, src)], 0
    while heap:
        d, u = heapq.heappop(heap); pops += 1
        if d > dist.get(u, 1e9): continue
        if u == dst: break
        for v, w in g[u]:
            if d + w < dist.get(v, 1e9):
                dist[v], prev[v] = d + w, u
                heapq.heappush(heap, (d + w, v))
    path = [dst]
    while path[-1] != src: path.append(prev[path[-1]])
    return dist[dst], path[::-1], pops
print("normal traffic:", dijkstra("A", "F", graph))
graph["C"] = [("B", 1), ("D", 8), ("E", 10)]
graph["B"] = [("D", 25)]                                           # an accident slows B->D, weights update
print("after an incident on B->D:", dijkstra("A", "F", graph))
