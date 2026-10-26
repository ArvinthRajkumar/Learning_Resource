def transpose(m):
    return [list(row) for row in zip(*m)]

def rotate_clockwise(m):
    return [list(row) for row in zip(*m[::-1])]

def search_sorted_matrix(m, target):
    r, c = 0, len(m[0]) - 1               # start top-right
    while r < len(m) and c >= 0:
        if m[r][c] == target:
            return True
        if m[r][c] > target:
            c -= 1                         # too big: move left
        else:
            r += 1                         # too small: move down
    return False
