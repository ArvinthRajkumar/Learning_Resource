"""Problem (d): beamSearch.

score(seq) = start[seq[0]] + sum(transition[seq[i-1]][seq[i]]).
Keep the best beamWidth sequences after every step. Higher score wins.
Exactly equal scores: the lexicographically smaller token-id sequence wins.
All scores are multiples of 0.125, so float sums are exact and == is safe.
"""
from typing import List


class Solution:
    def beamSearch(self, start: List[float], transition: List[List[float]],
                   steps: int, beamWidth: int) -> List[int]:
        V = len(start)
        # (negated score, sequence): sorting ascending puts the higher score
        # first and, for equal scores, the lexicographically smaller list first
        beam = sorted((-start[v], [v]) for v in range(V))[:beamWidth]
        for _ in range(steps - 1):
            cand = []
            for neg, seq in beam:
                last = seq[-1]
                row = transition[last]
                for v in range(V):
                    cand.append((neg - row[v], seq + [v]))
            cand.sort()
            beam = cand[:beamWidth]
        return beam[0][1]
