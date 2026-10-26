def restore_ip(s):
    res, parts = [], []
    def go(i):
        if len(parts) == 4:
            if i == len(s):
                res.append(".".join(parts))
            return
        for size in (1, 2, 3):
            part = s[i:i + size]
            if len(part) < size or (len(part) > 1 and part[0] == "0") or int(part) > 255:
                continue
            parts.append(part)
            go(i + size)
            parts.pop()
    go(0)
    return res
