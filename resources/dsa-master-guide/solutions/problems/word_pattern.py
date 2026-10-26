def word_pattern(pattern, s):
    words = s.split()
    if len(words) != len(pattern):
        return False
    p2w, w2p = {}, {}
    for p, w in zip(pattern, words):
        if p2w.setdefault(p, w) != w or w2p.setdefault(w, p) != p:
            return False
    return True
