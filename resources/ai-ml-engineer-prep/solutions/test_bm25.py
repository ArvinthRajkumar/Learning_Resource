"""Tests for rankBm25: examples, hand-computed scores, edge cases, ties,
an independent reference, randomized comparison, timing, and variants."""
import math
import random
import time

from bm25 import Solution, tokenize
from bm25_variants import Bm25Index, idf_classic, rank_bm25_qtf

EX1 = [
    "Vector databases store embeddings for retrieval.",
    "Rerank the retrieved chunks with a cross-encoder.",
    "Kubernetes rollout with a canary deploy.",
    "Hybrid retrieval mixes BM25 with dense embeddings; BM25 helps exact terms.",
]


def reference_scores(docs, query, k1=1.2, b=0.75):
    """Literal formula, doc by doc, using list.count (no Counter)."""
    toks = [tokenize(d) for d in docs]
    terms = sorted(set(tokenize(query)))
    N = len(docs)
    avgdl = sum(len(t) for t in toks) / N
    out = []
    for D in toks:
        s = 0.0
        for t in terms:
            n = sum(1 for x in toks if t in x)
            idf = math.log(1 + (N - n + 0.5) / (n + 0.5))
            f = D.count(t)
            if f:
                s += idf * f * (k1 + 1) / (f + k1 * (1 - b + b * len(D) / avgdl))
        out.append(s)
    return out


def reference_rank(docs, query, k):
    if not tokenize(query) or not docs or sum(len(tokenize(d)) for d in docs) == 0:
        return []
    sc = reference_scores(docs, query)
    idx = [i for i in range(len(docs)) if sc[i] > 0]
    idx.sort(key=lambda i: (-sc[i], i))
    return idx[:k]


def test_examples():
    s = Solution()
    assert s.rankBm25(EX1, "BM25 retrieval embeddings", 3) == [3, 0]
    assert s.rankBm25(["the cat", "the cat", "a dog"], "cat", 5) == [0, 1]


def test_hand_numbers():
    # doc lengths 6, 8, 6, 11 -> avgdl 7.75 ("cross-encoder" is two tokens)
    assert [len(tokenize(d)) for d in EX1] == [6, 8, 6, 11]
    sc = reference_scores(EX1, "BM25 retrieval embeddings")
    idf1 = math.log(1 + (4 - 1 + 0.5) / (1 + 0.5))   # bm25: in 1 doc
    idf2 = math.log(1 + (4 - 2 + 0.5) / (2 + 0.5))   # retrieval, embeddings: in 2 docs
    assert abs(idf1 - 1.2039728043259361) < 1e-12
    assert abs(idf2 - math.log(2)) < 1e-12
    # doc 0: retrieval f=1, embeddings f=1, |D|=6
    norm0 = 1.2 * (1 - 0.75 + 0.75 * 6 / 7.75)
    assert abs(sc[0] - 2 * idf2 * 2.2 / (1 + norm0)) < 1e-12
    assert sc[1] == 0.0 and sc[2] == 0.0   # "retrieved" is not "retrieval"
    assert sc[3] > sc[0] > 0


def test_edge_cases():
    s = Solution()
    assert s.rankBm25([], "x", 3) == []
    assert s.rankBm25(["a b"], "", 3) == []
    assert s.rankBm25(["a b"], "!!! ???", 3) == []           # no query tokens
    assert s.rankBm25(["", ""], "a", 3) == []                 # all docs empty
    assert s.rankBm25(["a b", "c"], "zzz", 3) == []           # nothing matches
    assert s.rankBm25(["a b", "a"], "a", 0) == []
    assert s.rankBm25(["a b", "a"], "a a A", 5) == [1, 0]     # distinct terms only; shorter doc wins
    assert s.rankBm25(["x", "a", "a", "a"], "a", 2) == [1, 2]  # k truncation keeps ties in index order
    # term in every doc still has positive idf, so it still counts
    assert s.rankBm25(["a", "a b"], "a", 5) == [0, 1]


def test_float_ties_identical_docs():
    s = Solution()
    # same words in different order -> same counts and length -> identical floats
    docs = ["retrieval beam kv cache"] * 3 + ["cache kv beam retrieval", "kv", "retrieval kv kv"]
    out = s.rankBm25(docs, "kv retrieval cache beam", 10)
    top = out[:4]
    assert top == [0, 1, 2, 3], out


def test_randomized_against_reference():
    rng = random.Random(11)
    s = Solution()
    vocab = ["bm25", "rrf", "kv", "Cache", "beam", "lora", "x", "y", "retrieval", "retrieved"]
    for _ in range(2000):
        n = rng.randint(0, 8)
        docs = []
        for _ in range(n):
            if docs and rng.random() < 0.3:
                w = docs[rng.randrange(len(docs))].split()
                rng.shuffle(w)
                docs.append(" ".join(w))                     # permuted copy -> exact tie
            else:
                docs.append(" ".join(rng.choice(vocab) for _ in range(rng.randint(0, 8))))
        q = " ".join(rng.choice(vocab + ["??"]) for _ in range(rng.randint(0, 4)))
        k = rng.randint(0, 6)
        assert s.rankBm25(docs, q, k) == reference_rank(docs, q, k), (docs, q, k)
        assert Bm25Index(docs).search(q, k) == reference_rank(docs, q, k)
        assert rank_bm25_qtf(docs, " ".join(sorted(set(tokenize(q)))), k) == reference_rank(docs, q, k)


def test_performance():
    rng = random.Random(2)
    vocab = [f"t{i}" for i in range(3000)]
    docs = [" ".join(rng.choice(vocab) for _ in range(200)) for _ in range(1000)]
    t0 = time.perf_counter()
    for _ in range(5):
        Solution().rankBm25(docs, "t1 t2 t3 t4 t5 t6 t7 t8 t9 t10", 10)
    dt = (time.perf_counter() - t0) / 5
    assert dt < 1.0, dt
    return dt


def test_variants():
    # repeated query term changes the ranking under qtf weighting
    docs = ["kv kv kv", "beam beam beam"]
    assert Solution().rankBm25(docs, "kv beam beam", 2) == [0, 1]        # tie -> index order
    assert rank_bm25_qtf(docs, "kv beam beam", 2) == [1, 0]             # beam counted twice
    assert idf_classic(10, 8) < 0                                         # common term goes negative
    assert math.log(1 + (10 - 8 + 0.5) / (8 + 0.5)) > 0


if __name__ == "__main__":
    test_examples()
    test_hand_numbers()
    test_edge_cases()
    test_float_ties_identical_docs()
    test_randomized_against_reference()
    dt = test_performance()
    test_variants()
    print(f"bm25: all tests passed (2000 randomized cases x 3 implementations; 1000 docs x 200 tokens in {dt*1000:.0f} ms)")
