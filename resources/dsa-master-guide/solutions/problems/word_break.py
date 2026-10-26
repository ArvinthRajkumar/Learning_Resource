def word_break(s, words):
    word_set = set(words)
    ok = [True] + [False] * len(s)
    for i in range(1, len(s) + 1):
        for j in range(i):
            if ok[j] and s[j:i] in word_set:
                ok[i] = True
                break
    return ok[len(s)]
