"""Tests for packContext: examples, edge cases, an independent reference
implementation (Fraction-based Jaccard, different control flow), randomized
comparison, a timing check, and the variants."""
import itertools
import random
import re
import time
from fractions import Fraction

from pack_context import Solution, near_duplicate, word_set
from pack_context_variants import Variants, pack_prefix_filter


def reference(chunks, scores, tokens, budget):
    """Independent re-implementation: exact Fraction Jaccard, explicit loops."""
    def words(t):
        out, cur = set(), ""
        for ch in t.lower():
            if ("a" <= ch <= "z") or ("0" <= ch <= "9"):
                cur += ch
            else:
                if cur:
                    out.add(cur)
                cur = ""
        if cur:
            out.add(cur)
        return out

    def jacc_ok(a, b):
        if not a and not b:
            return True
        return Fraction(len(a & b), len(a | b)) >= Fraction(4, 5)

    idx = list(range(len(chunks)))
    # stable sort by index first, then by score descending
    idx.sort()
    idx.sort(key=lambda i: scores[i], reverse=True)
    picked, left = [], budget
    for i in idx:
        wi = words(chunks[i])
        if tokens[i] <= left and all(not jacc_ok(wi, words(chunks[j])) for j in picked):
            picked.append(i)
            left -= tokens[i]
    return sorted(picked)


def test_examples():
    s = Solution()
    chunks = [
        "LoRA trains low-rank adapters while the base model stays frozen.",
        "LoRA trains low rank adapters; the base model stays frozen!",
        "Quantization to 4-bit cuts memory bandwidth during decoding.",
        "Rerankers reorder retrieved passages by relevance.",
    ]
    assert s.packContext(chunks, [0.9, 0.85, 0.7, 0.6], [120, 115, 300, 90], 450) == [0, 2]
    a, b = word_set(chunks[0]), word_set(chunks[1])
    assert (len(a & b), len(a | b)) == (10, 11)  # 5*10 = 50 >= 44 = 4*11
    assert s.packContext(["a b c d e", "x y z", "a b c d"], [0.5, 0.5, 0.4], [10, 10, 5], 20) == [0, 1]


def test_edge_cases():
    s = Solution()
    assert s.packContext([], [], [], 100) == []
    assert s.packContext(["abc"], [1.0], [5], 4) == []          # does not fit
    assert s.packContext(["abc"], [1.0], [5], 5) == [0]         # exactly fits
    assert s.packContext(["!!!", "???"], [1.0, 0.9], [1, 1], 10) == [0]  # two empty sets are near-duplicates
    assert s.packContext(["", "a"], [1.0, 0.9], [1, 1], 10) == [0, 1]    # empty vs non-empty: 0 >= 4 is false
    assert s.packContext(["x", "y"], [0.5, 0.5], [3, 3], 3) == [0]       # tie broken by smaller index
    # skip-but-continue: chunk 1 does not fit, chunk 2 still does
    assert s.packContext(["a", "b", "c"], [0.9, 0.8, 0.7], [5, 10, 3], 9) == [0, 2]
    # zero-token chunks are always affordable
    assert s.packContext(["a", "b"], [0.9, 0.8], [0, 0], 0) == [0, 1]
    # uppercase and punctuation fold into the same words
    assert word_set("Hello, WORLD-42!") == {"hello", "world", "42"}
    # exactly 0.8 counts (4 shared of 5 total)
    assert near_duplicate({"a", "b", "c", "d"}, {"a", "b", "c", "d", "e"})
    assert not near_duplicate({"a", "b", "c"}, {"a", "b", "c", "d"})  # 3/4 = 0.75 < 0.8


def test_randomized_against_reference():
    rng = random.Random(7)
    s = Solution()
    vocab = ["lora", "rank", "kv", "cache", "bm25", "rrf", "Gpu", "token", "beam", "x1", "y2", "z3"]
    for _ in range(3000):
        n = rng.randint(0, 12)
        chunks = []
        for _ in range(n):
            if chunks and rng.random() < 0.35:
                base = rng.choice(chunks).split()   # make near-duplicates likely
                if base and rng.random() < 0.5:
                    base.pop(rng.randrange(len(base)))
                chunks.append(" ".join(base) + rng.choice(["", "!", ";", " ."]))
            else:
                k = rng.randint(0, 7)
                chunks.append(rng.choice([" ", ",", "-", "  "]).join(rng.choice(vocab) for _ in range(k)))
        scores = [rng.choice([0.1, 0.5, 0.5, 0.9, 0.3]) for _ in range(n)]
        tokens = [rng.randint(0, 60) for _ in range(n)]
        budget = rng.randint(0, 150)
        expected = reference(chunks, scores, tokens, budget)
        assert s.packContext(chunks, scores, tokens, budget) == expected
        assert pack_prefix_filter(chunks, scores, tokens, budget) == expected


def test_performance():
    rng = random.Random(1)
    vocab = [f"w{i}" for i in range(5000)]
    chunks = [" ".join(rng.choice(vocab) for _ in range(300)) for _ in range(1000)]
    scores = [rng.random() for _ in range(1000)]
    tokens = [1] * 1000                     # worst case: everything fits, so every chunk is compared
    t0 = time.perf_counter()
    out = Solution().packContext(chunks, scores, tokens, 10**9)
    dt = time.perf_counter() - t0
    assert len(out) == 1000
    assert dt < 10, dt
    return dt


def test_variants():
    v = Variants()
    # stop-at-first-miss differs from skip-and-continue
    assert v.packStopAtFirstMiss(["a", "b", "c"], [0.9, 0.8, 0.7], [5, 10, 3], 9) == [0]
    assert Solution().packContext(["a", "b", "c"], [0.9, 0.8, 0.7], [5, 10, 3], 9) == [0, 2]
    # per-source cap
    out = v.packPerSourceCap(["a", "b", "c", "d"], [0.9, 0.8, 0.7, 0.6], [1, 1, 1, 1], 10,
                             ["doc1", "doc1", "doc1", "doc2"], 2)
    assert out == [0, 1, 3]
    # knapsack beats greedy and matches brute force
    assert v.packOptimalScore([0.9, 0.8, 0.8], [400, 200, 200], 400) == [1, 2]
    rng = random.Random(3)
    for _ in range(300):
        n = rng.randint(0, 8)
        sc = [rng.randint(1, 20) / 4 for _ in range(n)]
        tk = [rng.randint(1, 15) for _ in range(n)]
        bud = rng.randint(0, 40)
        got = v.packOptimalScore(sc, tk, bud)
        assert sum(tk[i] for i in got) <= bud
        best = max(sum(sc[i] for i in sub)
                   for r in range(n + 1) for sub in itertools.combinations(range(n), r)
                   if sum(tk[i] for i in sub) <= bud)
        assert abs(sum(sc[i] for i in got) - best) < 1e-9


if __name__ == "__main__":
    test_examples()
    test_edge_cases()
    test_randomized_against_reference()
    dt = test_performance()
    test_variants()
    print(f"pack_context: all tests passed (3000 randomized cases vs reference; worst case 1000x300 words in {dt:.2f}s)")
