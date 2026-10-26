def flood_fill(image, sr, sc, new_color):
    old = image[sr][sc]
    if old == new_color:
        return image
    def dfs(r, c):
        if 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == old:
            image[r][c] = new_color
            dfs(r + 1, c); dfs(r - 1, c); dfs(r, c + 1); dfs(r, c - 1)
    dfs(sr, sc)
    return image
