"""Problem (a): packContext.

Greedy context packing under a token budget with near-duplicate removal.
Visit chunks by score descending (ties: smaller index first). Skip a chunk
that does not fit the remaining budget, skip a near-duplicate of an already
picked chunk, otherwise pick it. Return picked indices in ascending order.
"""
import re
from typing import List

WORD_RE = re.compile(r"[a-z0-9]+")


def word_set(text: str) -> set:
    """Lowercase, then every maximal run of [a-z0-9] is one word."""
    return set(WORD_RE.findall(text.lower()))


def near_duplicate(a: set, b: set) -> bool:
    """Jaccard(a, b) >= 0.8, tested in integers: 5*|A&B| >= 4*|A|B|.

    Two empty sets give 0 >= 0, so they count as near-duplicates without a
    special case.
    """
    inter = len(a & b)
    union = len(a) + len(b) - inter
    return 5 * inter >= 4 * union


class Solution:
    def packContext(self, chunks: List[str], scores: List[float],
                    tokens: List[int], budget: int) -> List[int]:
        n = len(chunks)
        order = sorted(range(n), key=lambda i: (-scores[i], i))
        sets = [word_set(c) for c in chunks]
        remaining = budget
        picked: List[int] = []
        for i in order:
            if tokens[i] > remaining:
                continue  # does not fit, but a later, smaller chunk might
            a = sets[i]
            dup = False
            for j in picked:
                b = sets[j]
                # cheap size filter: |A&B| <= min and |A|B| >= max, so a
                # near-duplicate needs 5*min >= 4*max
                small, large = min(len(a), len(b)), max(len(a), len(b))
                if 5 * small < 4 * large:
                    continue
                if near_duplicate(a, b):
                    dup = True
                    break
            if dup:
                continue
            picked.append(i)
            remaining -= tokens[i]
        return sorted(picked)
