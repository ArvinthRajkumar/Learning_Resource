from collections import Counter

def most_frequent_word(words):
    freq = Counter(words)
    return min(freq, key=lambda w: (-freq[w], w))
