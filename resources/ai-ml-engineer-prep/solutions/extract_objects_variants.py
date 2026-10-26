"""Variants of problem (c) extractObjects."""
import json
from typing import Any, List, Tuple

from extract_objects import Solution


def extract_valid(chunks: List[str]) -> List[Any]:
    """Variant 1: return parsed objects, skipping spans that are not valid JSON.

    The scanner only balances braces; it does not check commas, colons or
    literals. json.loads on each span is the cheap way to add validation.
    """
    out = []
    for span in Solution().extractObjects(chunks):
        try:
            out.append(json.loads(span))
        except json.JSONDecodeError:
            pass
    return out


def extract_values(chunks: List[str]) -> List[str]:
    """Variant 2: top-level objects AND arrays.

    Keep a stack of expected closers instead of a counter, so "{]" style
    mismatches can be detected. Here a mismatch abandons the current value
    and the scan goes back to "outside".
    """
    text = "".join(chunks)
    pair = {"{": "}", "[": "]"}
    out, stack, start = [], [], -1
    in_str = esc = False
    for i, ch in enumerate(text):
        if not stack:
            if ch in pair:
                stack, start = [pair[ch]], i
            continue
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch in pair:
            stack.append(pair[ch])
        elif ch in "}]":
            if ch != stack[-1]:
                stack = []                 # mismatched closer: drop this value
                continue
            stack.pop()
            if not stack:
                out.append(text[start:i + 1])
    return out


def extract_spans(chunks: List[str]) -> List[Tuple[int, int]]:
    """Variant 3: (start, end_exclusive) offsets into the joined text.

    Useful when the caller wants to strip the JSON out of the surrounding
    prose, or to report positions. Same scanner, different output.
    """
    text = "".join(chunks)
    spans, depth, start = [], 0, -1
    in_str = esc = False
    for i, ch in enumerate(text):
        if depth == 0:
            if ch == "{":
                depth, start = 1, i
            continue
        if in_str:
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == '"':
                in_str = False
            continue
        if ch == '"':
            in_str = True
        elif ch == "{":
            depth += 1
        elif ch == "}":
            depth -= 1
            if depth == 0:
                spans.append((start, i + 1))
    return spans
