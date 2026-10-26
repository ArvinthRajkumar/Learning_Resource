from collections import deque

def word_ladder(begin, end, words):
    words = set(words)
    if end not in words:
        return 0
    q = deque([(begin, 1)])
    while q:
        word, steps = q.popleft()
        if word == end:
            return steps
        for i in range(len(word)):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                nxt = word[:i] + ch + word[i + 1:]
                if nxt in words:
                    words.remove(nxt)               # visited
                    q.append((nxt, steps + 1))
    return 0
