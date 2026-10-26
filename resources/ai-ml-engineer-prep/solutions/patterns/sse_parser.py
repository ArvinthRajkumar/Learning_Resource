"""Incremental Server-Sent Events parser (the wire format LLM APIs stream over)."""
import re
from typing import Dict, List, Optional

_EOL = re.compile(r"\r\n|\r|\n")


class SSEParser:
    """feed(chunk) -> list of complete events {"event", "data", "id"}.

    Rules (from the HTML Living Standard's EventSource section):
    - Lines end with \\n, \\r\\n or \\r. A chunk may end mid-line, or between \\r and \\n.
    - A blank line dispatches the event if any data was collected.
    - "field: value": one leading space after the colon is removed.
    - "data" lines are joined with \\n. A line starting with ":" is a comment.
    - Event type defaults to "message". "id" persists across events.
    """

    def __init__(self) -> None:
        self.buf = ""
        self.data: List[str] = []
        self.event = ""
        self.last_id = ""
        self.retry: Optional[int] = None
        self._skip_lf = False

    def feed(self, chunk: str) -> List[Dict[str, str]]:
        out: List[Dict[str, str]] = []
        if chunk and self._skip_lf:
            if chunk.startswith("\n"):
                chunk = chunk[1:]
            self._skip_lf = False
        self.buf += chunk
        while True:
            m = _EOL.search(self.buf)
            if not m:
                break
            line = self.buf[:m.start()]
            if m.group() == "\r" and m.end() == len(self.buf):
                self._skip_lf = True            # a "\n" at the start of the next chunk belongs to this "\r"
            self.buf = self.buf[m.end():]
            ev = self._line(line)
            if ev:
                out.append(ev)
        return out

    def _line(self, line: str) -> Optional[Dict[str, str]]:
        if line == "":
            if not self.data:
                self.event = ""
                return None
            ev = {"event": self.event or "message", "data": "\n".join(self.data), "id": self.last_id}
            self.data, self.event = [], ""
            return ev
        if line.startswith(":"):
            return None                        # comment / keep-alive
        field, sep, value = line.partition(":")
        if sep and value.startswith(" "):
            value = value[1:]
        if field == "data":
            self.data.append(value)
        elif field == "event":
            self.event = value
        elif field == "id" and "\0" not in value:
            self.last_id = value
        elif field == "retry" and value.isdigit():
            self.retry = int(value)
        return None
