"""Tests for beamSearch: examples, brute-force verifier, an independent
reference implementation, randomized comparison, global-optimum checks,
timing at the limits, and the variants."""
import functools
import itertools
import random
import time

from beam_search import Solution
from beam_search_variants import beam_top_n, beam_with_eos, viterbi_best

START = [-0.5, -1.0, -6.0]
TRANS = [[-2.0, -2.0, -2.0], [-0.25, -0.125, -6.0], [-6.0, -6.0, -6.0]]


def seq_score(start, trans, seq):
    s = start[seq[0]]
    for a, b in zip(seq, seq[1:]):
        s += trans[a][b]
    return s


def brute_force(start, trans, steps):
    """Global optimum over all V^steps sequences, same tie-break."""
    V = len(start)
    return min(itertools.product(range(V), repeat=steps),
               key=lambda seq: (-seq_score(start, trans, seq), seq))


def reference_beam(start, trans, steps, width):
    """Independent implementation: comparator function, tuples, recomputed scores."""
    def cmp(x, y):
        sx, sy = seq_score(start, trans, x), seq_score(start, trans, y)
        if sx != sy:
            return -1 if sx > sy else 1
        return -1 if x < y else (1 if x > y else 0)

    key = functools.cmp_to_key(cmp)
    beam = sorted([(v,) for v in range(len(start))], key=key)[:width]
    for _ in range(steps - 1):
        beam = sorted([s + (v,) for s in beam for v in range(len(start))], key=key)[:width]
    return list(beam[0])


def rand_problem(rng, V, steps):
    q = lambda: rng.randint(-48, 0) * 0.125   # multiples of 0.125, ties are common
    return [q() for _ in range(V)], [[q() for _ in range(V)] for _ in range(V)]


def test_examples():
    s = Solution()
    assert s.beamSearch(START, TRANS, 3, 1) == [0, 0, 0]
    assert seq_score(START, TRANS, [0, 0, 0]) == -4.5
    assert s.beamSearch(START, TRANS, 3, 2) == [1, 1, 1]
    assert seq_score(START, TRANS, [1, 1, 1]) == -1.25
    assert list(brute_force(START, TRANS, 3)) == [1, 1, 1]   # width 2 happens to find the optimum


def test_edge_cases():
    s = Solution()
    assert s.beamSearch([0.0], [[0.0]], 1, 1) == [0]
    assert s.beamSearch([0.0], [[-1.0]], 5, 3) == [0, 0, 0, 0, 0]
    assert s.beamSearch([-1.0, -1.0], [[0.0, 0.0], [0.0, 0.0]], 1, 1) == [0]   # tie -> smaller id
    assert s.beamSearch([-1.0, -0.5], [[0.0, 0.0], [0.0, 0.0]], 1, 10) == [1]   # steps = 1: best start
    # all-equal scores everywhere: answer is all zeros
    assert s.beamSearch([0.0] * 4, [[0.0] * 4] * 4, 6, 2) == [0] * 6
    # beamWidth larger than the number of candidates is fine
    assert s.beamSearch(START, TRANS, 2, 10) == list(brute_force(START, TRANS, 2))


def test_beam_misses_optimum():
    # greedy (width 1) commits to token 0 because -0.5 > -1.0 and never recovers
    assert seq_score(START, TRANS, Solution().beamSearch(START, TRANS, 3, 1)) < seq_score(START, TRANS, brute_force(START, TRANS, 3))


def test_randomized_against_reference_and_brute():
    rng = random.Random(2024)
    s = Solution()
    misses = 0
    for _ in range(1500):
        V, steps, width = rng.randint(1, 4), rng.randint(1, 5), rng.randint(1, 5)
        st, tr = rand_problem(rng, V, steps)
        got = s.beamSearch(st, tr, steps, width)
        assert got == reference_beam(st, tr, steps, width)
        best = list(brute_force(st, tr, steps))
        assert seq_score(st, tr, got) <= seq_score(st, tr, best)
        if width >= V ** (steps - 1):            # nothing pruned before the last pick
            assert got == best
        if got != best:
            misses += 1
        assert viterbi_best(st, tr, steps) == best
    return misses


def test_limits_timing():
    rng = random.Random(9)
    st, tr = rand_problem(rng, 50, 30)
    t0 = time.perf_counter()
    out = Solution().beamSearch(st, tr, 30, 10)
    dt = time.perf_counter() - t0
    assert len(out) == 30 and out == reference_beam(st, tr, 30, 10)
    assert dt < 1.0
    return dt


def test_variants():
    top = beam_top_n(START, TRANS, 3, 2, 2)
    assert top == [(-1.25, [1, 1, 1]), (-1.375, [1, 1, 0])]
    # eos: token 2 is EOS. Without normalization the short [2] wins; with it a longer answer can win.
    lp_start = [-0.5, -3.0, -1.0]
    lp_next = [[-0.1, -3.0, -0.6], [-1.0, -1.0, -1.0], [-9.0, -9.0, -9.0]]
    assert beam_with_eos(lp_start, lp_next, eos=2, max_len=4, beamWidth=3, alpha=0.0) == [2]
    assert beam_with_eos(lp_start, lp_next, eos=2, max_len=4, beamWidth=3, alpha=1.0) == [0, 0, 0, 2]


if __name__ == "__main__":
    test_examples()
    test_edge_cases()
    test_beam_misses_optimum()
    misses = test_randomized_against_reference_and_brute()
    dt = test_limits_timing()
    test_variants()
    print(f"beam_search: all tests passed (1500 randomized vs reference + brute force + Viterbi; beam missed the optimum in {misses} cases; V=50 steps=30 width=10 in {dt*1000:.0f} ms)")
