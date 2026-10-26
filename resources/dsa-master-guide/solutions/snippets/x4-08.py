from collections import deque
def aho_corasick(patterns, text):
    goto, fail, out = [{}], [0], [[]]
    for idx, p in enumerate(patterns):
        s = 0
        for ch in p:
            if ch not in goto[s]:
                goto.append({}); fail.append(0); out.append([])
                goto[s][ch] = len(goto) - 1
            s = goto[s][ch]
        out[s].append(idx)
    q = deque(goto[0].values())
    while q:
        u = q.popleft()
        for ch, v in goto[u].items():
            f = fail[u]
            while f and ch not in goto[f]: f = fail[f]
            fail[v] = goto[f].get(ch, 0) if goto[f].get(ch, 0) != v else 0
            out[v] = out[v] + out[fail[v]]
            q.append(v)
    s, found = 0, []
    for i, ch in enumerate(text):
        while s and ch not in goto[s]: s = fail[s]
        s = goto[s].get(ch, 0)
        for idx in out[s]: found.append((i - len(patterns[idx]) + 1, patterns[idx]))
    return sorted(found)
pats = ["he", "she", "his", "hers"]
text = "ushers"
expected = sorted((i, p) for p in pats for i in range(len(text)) if text.startswith(p, i))
print(aho_corasick(pats, text), aho_corasick(pats, text) == expected)
