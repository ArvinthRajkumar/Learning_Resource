from collections import deque

def pacific_atlantic(heights):
    R, C = len(heights), len(heights[0])
    def reach(starts):
        seen, q = set(starts), deque(starts)
        while q:
            r, c = q.popleft()
            for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and (nr, nc) not in seen and heights[nr][nc] >= heights[r][c]:
                    seen.add((nr, nc))
                    q.append((nr, nc))
        return seen
    pac = reach([(0, c) for c in range(C)] + [(r, 0) for r in range(1, R)])
    atl = reach([(R - 1, c) for c in range(C)] + [(r, C - 1) for r in range(R - 1)])
    return sorted([r, c] for r, c in pac & atl)
