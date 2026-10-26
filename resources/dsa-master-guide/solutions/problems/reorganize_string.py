import heapq
from collections import Counter

def reorganize_string(s):
    heap = [(-c, ch) for ch, c in Counter(s).items()]
    heapq.heapify(heap)
    out, prev = [], (0, "")
    while heap:
        c, ch = heapq.heappop(heap)
        out.append(ch)
        if prev[0] < 0:
            heapq.heappush(heap, prev)      # the held-back letter returns
        prev = (c + 1, ch)
    res = "".join(out)
    return res if len(res) == len(s) else ""
