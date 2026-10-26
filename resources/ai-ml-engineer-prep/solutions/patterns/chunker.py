"""Fixed-size text chunker with overlap."""
from typing import List, Sequence


def chunk_tokens(tokens: Sequence, size: int, overlap: int) -> List[Sequence]:
    """Windows of `size` tokens; consecutive windows share `overlap` tokens.

    step = size - overlap. Stops once a window reaches the end, so the tail
    is covered exactly once and no tiny duplicate chunk is produced.
    Number of chunks for n > size: 1 + ceil((n - size) / step).
    """
    if size <= 0 or not 0 <= overlap < size:
        raise ValueError("need size > 0 and 0 <= overlap < size")
    step = size - overlap
    out = []
    start = 0
    while True:
        out.append(tokens[start:start + size])
        if start + size >= len(tokens):
            break
        start += step
    return out if len(tokens) else []


def chunk_words(text: str, size: int, overlap: int) -> List[str]:
    """Whitespace-word version (real pipelines count model tokens, and prefer
    splitting on sentence or heading boundaries)."""
    return [" ".join(c) for c in chunk_tokens(text.split(), size, overlap)]
