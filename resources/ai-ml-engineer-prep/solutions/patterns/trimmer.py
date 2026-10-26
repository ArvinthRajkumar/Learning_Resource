"""Sliding-window token budget trimmer for chat history."""
from typing import Callable, Dict, List


def trim_history(messages: List[Dict[str, str]], budget: int,
                 count_tokens: Callable[[str], int]) -> List[Dict[str, str]]:
    """Keep system messages and the newest messages that fit; drop the oldest.

    - System messages are always kept (they carry the instructions).
    - Walk the rest from newest to oldest and keep each whole message while it
      fits; stop at the first one that does not (never skip a gap, which would
      break the conversation's order of events).
    - The newest message must fit, otherwise raise: silently dropping the
      user's actual question is the worst possible failure.
    Returns kept messages in their original order.
    """
    system = [i for i, m in enumerate(messages) if m["role"] == "system"]
    used = sum(count_tokens(messages[i]["content"]) for i in system)
    if used > budget:
        raise ValueError("system messages alone exceed the budget")
    keep = set(system)
    others = [i for i in range(len(messages)) if i not in keep]
    for n, i in enumerate(reversed(others)):
        cost = count_tokens(messages[i]["content"])
        if used + cost > budget:
            if n == 0:
                raise ValueError("newest message does not fit in the budget")
            break
        used += cost
        keep.add(i)
    return [messages[i] for i in sorted(keep)]
