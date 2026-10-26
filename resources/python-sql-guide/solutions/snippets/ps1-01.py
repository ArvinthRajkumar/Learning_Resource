import re
from collections import Counter

def top_words(text, k):
    words = re.findall(r"[a-z']+", text.lower())
    counts = Counter(words)
    return sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))[:k]

print(top_words("The cat and the hat. The bat sat; the cat ran!", 3))
