"""LRU cache, and a block-level prefix cache built on it (the idea behind prompt/prefix caching)."""
from collections import OrderedDict
from typing import Hashable, List, Optional, Sequence


class LRUCache:
    """O(1) get/put. OrderedDict keeps keys in recency order; the front is least recent."""

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be >= 1")
        self.capacity = capacity
        self.data: "OrderedDict[Hashable, object]" = OrderedDict()

    def get(self, key: Hashable) -> Optional[object]:
        if key not in self.data:
            return None
        self.data.move_to_end(key)          # mark as most recently used
        return self.data[key]

    def put(self, key: Hashable, value: object) -> Optional[Hashable]:
        """Insert or update. Returns the evicted key, if any."""
        if key in self.data:
            self.data.move_to_end(key)
            self.data[key] = value
            return None
        self.data[key] = value
        if len(self.data) > self.capacity:
            evicted, _ = self.data.popitem(last=False)
            return evicted
        return None


class PrefixCache:
    """Caches prompt prefixes in fixed-size token blocks, keyed by the whole prefix.

    The key for block j is the tuple of ALL tokens up to the end of block j,
    so a block is only reused when everything before it matches too. That
    is why prompt caching only helps with a shared PREFIX: change one early
    token and every later block key changes. Real servers hash the prefix
    instead of storing the tuple (vLLM-style automatic prefix caching works
    on this block principle; details vary by server and version).
    """

    def __init__(self, block: int, capacity_blocks: int):
        self.block = block
        self.lru = LRUCache(capacity_blocks)

    def _keys(self, tokens: Sequence[int]) -> List[tuple]:
        full = len(tokens) // self.block
        return [tuple(tokens[:(j + 1) * self.block]) for j in range(full)]

    def lookup(self, tokens: Sequence[int]) -> int:
        """Number of leading tokens whose KV could be reused (block aligned)."""
        hit = 0
        for key in self._keys(tokens):
            if self.lru.get(key) is None:
                break
            hit += self.block
        return hit

    def insert(self, tokens: Sequence[int]) -> None:
        for key in self._keys(tokens):
            self.lru.put(key, True)
