from functools import lru_cache

def longest_inc_path_matrix(matrix):
    R, C = len(matrix), len(matrix[0])
    @lru_cache(maxsize=None)
    def go(r, c):
        best = 1
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C and matrix[nr][nc] > matrix[r][c]:
                best = max(best, 1 + go(nr, nc))
        return best
    return max(go(r, c) for r in range(R) for c in range(C))
