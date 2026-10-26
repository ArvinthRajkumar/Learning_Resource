def palindrome_partitions(s):
    res, path = [], []
    def go(start):
        if start == len(s):
            res.append(path[:])
            return
        for end in range(start + 1, len(s) + 1):
            piece = s[start:end]
            if piece == piece[::-1]:       # only continue if the piece is a palindrome
                path.append(piece)
                go(end)
                path.pop()
    go(0)
    return res
