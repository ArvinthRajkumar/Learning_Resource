"""Variants of problem (a) packContext."""
from typing import List

from pack_context import near_duplicate, word_set


class Variants:
    def packStopAtFirstMiss(self, chunks: List[str], scores: List[float],
                            tokens: List[int], budget: int) -> List[int]:
        """Variant 1: stop the scan at the first chunk that does not fit.

        One word changes (continue becomes break) and the answer changes:
        a small, lower-scored chunk that would still fit is never considered.
        """
        order = sorted(range(len(chunks)), key=lambda i: (-scores[i], i))
        sets = [word_set(c) for c in chunks]
        remaining, picked = budget, []
        for i in order:
            if tokens[i] > remaining:
                break
            if any(near_duplicate(sets[i], sets[j]) for j in picked):
                continue
            picked.append(i)
            remaining -= tokens[i]
        return sorted(picked)

    def packPerSourceCap(self, chunks: List[str], scores: List[float],
                         tokens: List[int], budget: int,
                         sources: List[str], cap: int) -> List[int]:
        """Variant 2: same greedy, plus at most `cap` chunks per source doc.

        Common in production: stops one long document from filling the
        whole context. The cap check is just one more skip condition.
        """
        order = sorted(range(len(chunks)), key=lambda i: (-scores[i], i))
        sets = [word_set(c) for c in chunks]
        used = {}
        remaining, picked = budget, []
        for i in order:
            if tokens[i] > remaining:
                continue
            if used.get(sources[i], 0) >= cap:
                continue
            if any(near_duplicate(sets[i], sets[j]) for j in picked):
                continue
            picked.append(i)
            used[sources[i]] = used.get(sources[i], 0) + 1
            remaining -= tokens[i]
        return sorted(picked)

    def packOptimalScore(self, scores: List[float], tokens: List[int],
                         budget: int) -> List[int]:
        """Variant 3: maximize total score under the budget (0/1 knapsack).

        Greedy by score is not optimal: one 0.9 chunk of 400 tokens can
        block two 0.8 chunks of 200. DP over budget fixes that in
        O(n * budget). (With the near-duplicate rule added the exact problem
        becomes much harder, which is why production systems use greedy.)
        Ties in total score: the DP keeps the first solution found, which
        prefers not taking later items.
        """
        n = len(scores)
        best = [0.0] * (budget + 1)
        take = [[False] * (budget + 1) for _ in range(n)]
        for i in range(n):
            w, v = tokens[i], scores[i]
            for cap in range(budget, w - 1, -1):
                if best[cap - w] + v > best[cap]:
                    best[cap] = best[cap - w] + v
                    take[i][cap] = True
        cap, picked = budget, []
        for i in range(n - 1, -1, -1):
            if take[i][cap]:
                picked.append(i)
                cap -= tokens[i]
        return sorted(picked)


def pack_prefix_filter(chunks: List[str], scores: List[float],
                       tokens: List[int], budget: int) -> List[int]:
    """Variant 4: same output as packContext, faster when many chunks get picked.

    Prefix filtering (a standard similarity-join trick). If J(A, B) >= 0.8
    then |A&B| >= ceil(0.8 * |A|). Sort each set's words by a global order
    (rarest first). Any two sets sharing at least o words must share a word
    inside each set's first |X| - o + 1 words. So index only those prefix
    words of picked chunks and run the exact Jaccard test only on chunks
    that share a prefix word. Empty sets are tracked separately.
    """
    sets = [word_set(c) for c in chunks]
    df = {}
    for s in sets:
        for w in s:
            df[w] = df.get(w, 0) + 1
    rank = {w: (df[w], w) for w in df}           # rare words first, ties by text

    def prefix(s):
        if not s:
            return []
        need = -(-4 * len(s) // 5)               # ceil(4|S|/5)
        return sorted(s, key=rank.__getitem__)[:len(s) - need + 1]

    order = sorted(range(len(chunks)), key=lambda i: (-scores[i], i))
    index = {}                                    # prefix word -> picked chunk ids
    picked_empty = False
    remaining, picked = budget, []
    for i in order:
        if tokens[i] > remaining:
            continue
        a = sets[i]
        if not a:
            if picked_empty:
                continue
            dup = False
        else:
            pa = prefix(a)
            cands = set()
            for w in pa:
                cands.update(index.get(w, ()))
            dup = any(near_duplicate(a, sets[j]) for j in cands)
        if dup:
            continue
        picked.append(i)
        remaining -= tokens[i]
        if not a:
            picked_empty = True
        else:
            for w in pa:
                index.setdefault(w, []).append(i)
    return sorted(picked)
