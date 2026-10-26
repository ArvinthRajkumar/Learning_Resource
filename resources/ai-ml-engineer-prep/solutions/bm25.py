"""Problem (b): rankBm25.

Okapi BM25 with k1 = 1.2, b = 0.75 and the "plus one" idf
idf(t) = ln(1 + (N - n(t) + 0.5) / (n(t) + 0.5)), which is always > 0.
Return indices with score > 0, sorted by score desc then index asc, at most k.
"""
import math
import re
from collections import Counter
from typing import List

WORD_RE = re.compile(r"[a-z0-9]+")


def tokenize(text: str) -> List[str]:
    return WORD_RE.findall(text.lower())


class Solution:
    def rankBm25(self, docs: List[str], query: str, k: int) -> List[int]:
        k1, b = 1.2, 0.75
        terms = sorted(set(tokenize(query)))      # distinct terms, fixed order
        if not terms or not docs or k <= 0:
            return []
        N = len(docs)
        tfs = [Counter(tokenize(d)) for d in docs]
        lens = [sum(tf.values()) for tf in tfs]
        avgdl = sum(lens) / N
        if avgdl == 0:
            return []                             # every doc is empty: nothing can match
        idf = {}
        for t in terms:
            n_t = sum(1 for tf in tfs if t in tf)
            idf[t] = math.log(1 + (N - n_t + 0.5) / (n_t + 0.5))
        scored = []
        for i in range(N):
            tf, dl = tfs[i], lens[i]
            norm = k1 * (1 - b + b * dl / avgdl)
            s = 0.0
            # The score depends only on (f(t,D) for each query term, |D|) and is
            # summed in the same term order for every doc, so two docs with the
            # same counts and length get bit-identical floats and the index
            # tie-break is exact. No epsilon comparison needed.
            for t in terms:
                f = tf.get(t, 0)
                if f:
                    s += idf[t] * f * (k1 + 1) / (f + norm)
            if s > 0:
                scored.append((-s, i))
        scored.sort()
        return [i for _, i in scored[:k]]
