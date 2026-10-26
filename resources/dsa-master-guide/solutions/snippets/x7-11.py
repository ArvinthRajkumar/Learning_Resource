import random
from collections import deque
random.seed(10)
def islands(g):
    R, C, seen, count = len(g), len(g[0]), set(), 0
    for r in range(R):
        for c in range(C):
            if g[r][c] == 1 and (r, c) not in seen:
                count += 1
                stack = [(r, c)]; seen.add((r, c))
                while stack:
                    y, x = stack.pop()
                    for dy, dx in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ny, nx = y + dy, x + dx
                        if 0 <= ny < R and 0 <= nx < C and g[ny][nx] == 1 and (ny, nx) not in seen:
                            seen.add((ny, nx)); stack.append((ny, nx))
    return count
def islands_uf(g):
    R, C = len(g), len(g[0]); p = list(range(R * C))
    def f(x):
        while p[x] != x: p[x] = p[p[x]]; x = p[x]
        return x
    for r in range(R):
        for c in range(C):
            if g[r][c]:
                for dr, dc in ((1, 0), (0, 1)):
                    if r + dr < R and c + dc < C and g[r + dr][c + dc]: p[f(r * C + c)] = f((r + dr) * C + c + dc)
    return len({f(r * C + c) for r in range(R) for c in range(C) if g[r][c]})
for _ in range(200):
    g = [[random.randint(0, 1) for _ in range(5)] for _ in range(4)]
    assert islands(g) == islands_uf(g)
def ladder(begin, end, words):
    words, q = set(words), deque([(begin, 1)])
    while q:
        w, d = q.popleft()
        if w == end: return d
        for i in range(len(w)):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                nw = w[:i] + ch + w[i + 1:]
                if nw in words: words.remove(nw); q.append((nw, d + 1))
    return 0
print("islands verified two ways; ladder length:", ladder("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
