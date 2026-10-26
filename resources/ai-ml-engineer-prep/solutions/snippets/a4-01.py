from collections import Counter

def learn_bpe(words, merges):
    vocab = Counter(tuple(w) + ("</w>",) for w in words)      # each word as a tuple of symbols
    learned = []
    for _ in range(merges):
        pairs = Counter()
        for word, freq in vocab.items():
            for a, b in zip(word, word[1:]):
                pairs[(a, b)] += freq
        if not pairs:
            break
        best = max(pairs, key=lambda p: (pairs[p], p))         # most frequent, ties broken deterministically
        learned.append(best)
        new_vocab = Counter()
        for word, freq in vocab.items():
            out, i = [], 0
            while i < len(word):
                if i < len(word) - 1 and (word[i], word[i + 1]) == best:
                    out.append(word[i] + word[i + 1]); i += 2
                else:
                    out.append(word[i]); i += 1
            new_vocab[tuple(out)] += freq
        vocab = new_vocab
    return learned

def encode(word, merges):
    symbols = list(word) + ["</w>"]
    for a, b in merges:
        i = 0
        while i < len(symbols) - 1:
            if symbols[i] == a and symbols[i + 1] == b:
                symbols[i:i + 2] = [a + b]
            else:
                i += 1
    return symbols

corpus = ["low"] * 5 + ["lower"] * 2 + ["newest"] * 6 + ["widest"] * 3
merges = learn_bpe(corpus, 10)
print(merges[:5])
print(encode("lowest", merges))
print(encode("newer", merges))
