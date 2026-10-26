"""Variants of problem (b) rankBm25."""
import heapq
import math
from collections import Counter, defaultdict
from typing import Dict, List

from bm25 import tokenize


class Bm25Index:
    """Variant 1: build once, query many times (inverted index).

    Postings map term -> list of (doc id, term frequency). A query only
    touches docs that contain at least one query term, and heapq picks the
    top k in O(m log k) instead of sorting all m matches.
    Same ranking as Solution.rankBm25.
    """

    def __init__(self, docs: List[str], k1: float = 1.2, b: float = 0.75):
        self.k1, self.b = k1, b
        self.N = len(docs)
        self.postings: Dict[str, List[tuple]] = defaultdict(list)
        self.lens = []
        for i, d in enumerate(docs):
            tf = Counter(tokenize(d))
            self.lens.append(sum(tf.values()))
            for t, f in tf.items():
                self.postings[t].append((i, f))
        self.avgdl = (sum(self.lens) / self.N) if self.N else 0.0

    def idf(self, t: str) -> float:
        n_t = len(self.postings.get(t, ()))
        return math.log(1 + (self.N - n_t + 0.5) / (n_t + 0.5))

    def search(self, query: str, k: int) -> List[int]:
        terms = sorted(set(tokenize(query)))
        if not terms or self.avgdl == 0 or k <= 0:
            return []
        # accumulate per doc in the same term order as the reference solution
        partial: Dict[int, Dict[str, int]] = defaultdict(dict)
        for t in terms:
            for i, f in self.postings.get(t, ()):
                partial[i][t] = f
        scored = []
        for i, fmap in partial.items():
            norm = self.k1 * (1 - self.b + self.b * self.lens[i] / self.avgdl)
            s = 0.0
            for t in terms:
                f = fmap.get(t, 0)
                if f:
                    s += self.idf(t) * f * (self.k1 + 1) / (f + norm)
            if s > 0:
                scored.append((-s, i))
        return [i for _, i in heapq.nsmallest(k, scored)]


def rank_bm25_qtf(docs: List[str], query: str, k: int,
                  k1: float = 1.2, b: float = 0.75, k3: float = 8.0) -> List[int]:
    """Variant 2: query terms that repeat count more (Robertson's k3 factor).

    weight(t) = qtf * (k3 + 1) / (qtf + k3). With qtf = 1 the factor is 1,
    so a query without repeats ranks exactly like the base problem.
    """
    qtf = Counter(tokenize(query))
    if not qtf or not docs:
        return []
    terms = sorted(qtf)
    tfs = [Counter(tokenize(d)) for d in docs]
    lens = [sum(tf.values()) for tf in tfs]
    N, avgdl = len(docs), sum(lens) / len(docs)
    if avgdl == 0:
        return []
    out = []
    for i, tf in enumerate(tfs):
        norm = k1 * (1 - b + b * lens[i] / avgdl)
        s = 0.0
        for t in terms:
            f = tf.get(t, 0)
            if f:
                n_t = sum(1 for x in tfs if t in x)
                idf = math.log(1 + (N - n_t + 0.5) / (n_t + 0.5))
                s += idf * f * (k1 + 1) / (f + norm) * qtf[t] * (k3 + 1) / (qtf[t] + k3)
        if s > 0:
            out.append((-s, i))
    out.sort()
    return [i for _, i in out[:k]]


def idf_classic(N: int, n_t: int) -> float:
    """Variant 3 (for comparison): Robertson-Sparck Jones idf without the +1.

    ln((N - n + 0.5) / (n + 0.5)) goes negative when a term is in more than
    half the docs, so matching a very common word would LOWER the score.
    The +1 inside the log (Lucene's choice, used in this problem) keeps it > 0.
    """
    return math.log((N - n_t + 0.5) / (n_t + 0.5))
