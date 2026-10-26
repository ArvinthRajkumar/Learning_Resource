def region_size(grid, r, c, seen=None):
    seen = set() if seen is None else seen
    rows, cols = len(grid), len(grid[0])
    if not (0 <= r < rows and 0 <= c < cols):   # out of bounds
        return 0
    if grid[r][c] != "1" or (r, c) in seen:
        return 0
    seen.add((r, c))
    size = 1
    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        size += region_size(grid, r + dr, c + dc, seen)
    return size
