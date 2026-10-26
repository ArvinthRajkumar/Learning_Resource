"""Variants of problem (d) beamSearch."""
from typing import List, Optional, Tuple


def viterbi_best(start: List[float], transition: List[List[float]], steps: int) -> List[int]:
    """Variant 1: the exact global optimum, with the same tie-break rule.

    The score only depends on adjacent pairs (a first-order chain), so
    dynamic programming finds the true best in O(steps * V^2), no beam needed.
    To get the lexicographically smallest optimal sequence, run the DP
    BACKWARD: best[t][v] = best score of positions t..end given token v at t.
    Then walk forward, at each step taking the smallest token that still
    achieves the optimum. (A forward DP with back-pointers can break ties
    toward a lexicographically larger prefix.)
    """
    V = len(start)
    best = [[0.0] * V for _ in range(steps)]
    for t in range(steps - 2, -1, -1):
        for a in range(V):
            best[t][a] = max(transition[a][b] + best[t + 1][b] for b in range(V))
    total = max(start[v] + best[0][v] for v in range(V))
    seq = [min(v for v in range(V) if start[v] + best[0][v] == total)]
    for t in range(1, steps):
        a = seq[-1]
        need = best[t - 1][a]
        seq.append(min(b for b in range(V) if transition[a][b] + best[t][b] == need))
    return seq


def beam_top_n(start: List[float], transition: List[List[float]], steps: int,
               beamWidth: int, n: int) -> List[Tuple[float, List[int]]]:
    """Variant 2: return the final beam's best n (score, sequence) pairs.

    Used for n-best lists, reranking, or showing alternatives. n <= beamWidth.
    """
    V = len(start)
    beam = sorted((-start[v], [v]) for v in range(V))[:beamWidth]
    for _ in range(steps - 1):
        beam = sorted((neg - transition[s[-1]][v], s + [v])
                      for neg, s in beam for v in range(V))[:beamWidth]
    return [(-neg, s) for neg, s in beam[:n]]


def beam_with_eos(logp_start: List[float], logp_next: List[List[float]], eos: int,
                  max_len: int, beamWidth: int, alpha: float = 1.0) -> Optional[List[int]]:
    """Variant 3: beam search the way LLM decoders do it.

    Scores are log-probabilities (always <= 0), so longer sequences always
    score lower. A hypothesis that emits `eos` is finished and set aside.
    Finished hypotheses are compared by length-normalized score
    logp / len^alpha (alpha = 0 means no normalization, which favors short
    outputs). Returns the best finished sequence (eos included), or the best
    unfinished one if nothing finished within max_len.
    """
    V = len(logp_start)
    beam = sorted((-logp_start[v], [v]) for v in range(V))[:beamWidth]
    finished = []
    for _ in range(max_len):
        alive = []
        for neg, s in beam:
            if s[-1] == eos:
                finished.append((neg / (len(s) ** alpha), s))
            else:
                alive.append((neg, s))
        if not alive or len(alive[0][1]) == max_len:
            break
        beam = sorted((neg - logp_next[s[-1]][v], s + [v])
                      for neg, s in alive for v in range(V))[:beamWidth]
    else:
        alive = beam
    if finished:
        return min(finished)[1]
    return min(alive)[1] if alive else None
