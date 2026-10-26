"""Problem (c): extractObjects.

Pull complete top-level JSON objects out of a chunked text stream with a
single left-to-right state machine. Braces inside strings do not count.
A backslash inside a string escapes the next character. Objects are returned
exactly as they appear, in completion order. Unfinished objects are dropped.
"""
from typing import List


class Solution:
    def extractObjects(self, chunks: List[str]) -> List[str]:
        text = "".join(chunks)
        out: List[str] = []
        depth = 0           # 0 means "outside any object"
        start = -1          # index of the current top-level "{"
        in_str = False
        esc = False
        for i, ch in enumerate(text):
            if depth == 0:
                if ch == "{":
                    depth, start = 1, i
                continue                      # outside: ignore everything else
            if in_str:
                if esc:
                    esc = False               # this char is escaped, whatever it is
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
                    out.append(text[start:i + 1])
        return out


class StreamingExtractor:
    """Incremental version: call feed() with each chunk as it arrives.

    State (depth, in-string, pending escape, partial object) survives between
    calls, so a chunk may end anywhere, even right after a backslash.
    Memory is O(current object), not O(whole stream), and each object is
    returned the moment its closing brace arrives.
    """

    def __init__(self) -> None:
        self.depth = 0
        self.in_str = False
        self.esc = False
        self.buf: List[str] = []      # characters of the object in progress

    def feed(self, chunk: str) -> List[str]:
        done: List[str] = []
        for ch in chunk:
            if self.depth == 0:
                if ch == "{":
                    self.depth = 1
                    self.buf = ["{"]
                continue
            self.buf.append(ch)
            if self.in_str:
                if self.esc:
                    self.esc = False
                elif ch == "\\":
                    self.esc = True
                elif ch == '"':
                    self.in_str = False
                continue
            if ch == '"':
                self.in_str = True
            elif ch == "{":
                self.depth += 1
            elif ch == "}":
                self.depth -= 1
                if self.depth == 0:
                    done.append("".join(self.buf))
                    self.buf = []
        return done

    def pending(self) -> bool:
        """True if an object has started but not finished."""
        return self.depth > 0
