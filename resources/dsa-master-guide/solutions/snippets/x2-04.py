import heapq
def astar(grid, start, goal):
    h = lambda p: abs(p[0] - goal[0]) + abs(p[1] - goal[1])
    pq, g, expanded = [(h(start), 0, start)], {start: 0}, 0
    while pq:
        f, cost, cur = heapq.heappop(pq)
        if cost > g[cur]: continue
        expanded += 1
        if cur == goal: return cost, expanded
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            nxt = (cur[0] + dr, cur[1] + dc)
            if 0 <= nxt[0] < len(grid) and 0 <= nxt[1] < len(grid[0]) and grid[nxt[0]][nxt[1]] == 0:
                if cost + 1 < g.get(nxt, 10 ** 9):
                    g[nxt] = cost + 1
                    heapq.heappush(pq, (cost + 1 + h(nxt), cost + 1, nxt))
    return None, expanded
grid = [[0] * 20 for _ in range(20)]
for r in range(1, 18): grid[r][10] = 1             # a wall with gaps at the top and bottom
cost, expanded = astar(grid, (10, 0), (10, 19))
print("shortest path length", cost, "| A* expanded", expanded, "of", 20 * 20, "cells")
