"""One BPE training merge step."""
from collections import Counter
from typing import Dict, Optional, Tuple

Word = Tuple[str, ...]


def most_frequent_pair(vocab: Dict[Word, int]) -> Optional[Tuple[str, str]]:
    """Count adjacent symbol pairs weighted by word frequency.
    Ties: lexicographically smallest pair (real tokenizers pick their own rule)."""
    pairs: Counter = Counter()
    for word, freq in vocab.items():
        for a, b in zip(word, word[1:]):
            pairs[(a, b)] += freq
    if not pairs:
        return None
    best = max(pairs.values())
    return min(p for p, c in pairs.items() if c == best)


def merge_pair(vocab: Dict[Word, int], pair: Tuple[str, str]) -> Dict[Word, int]:
    """Replace every non-overlapping occurrence of pair, scanning left to right."""
    a, b = pair
    out: Dict[Word, int] = {}
    for word, freq in vocab.items():
        merged, i = [], 0
        while i < len(word):
            if i + 1 < len(word) and word[i] == a and word[i + 1] == b:
                merged.append(a + b)
                i += 2
            else:
                merged.append(word[i])
                i += 1
        key = tuple(merged)
        out[key] = out.get(key, 0) + freq
    return out


def bpe_step(vocab: Dict[Word, int]):
    """One training step: find the best pair and merge it. Returns (pair, new_vocab)."""
    pair = most_frequent_pair(vocab)
    if pair is None:
        return None, vocab
    return pair, merge_pair(vocab, pair)
