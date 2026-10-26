import re
from collections import Counter, defaultdict
LOG = """\
2024-03-01 10:00:01 GET /home 200 12ms
2024-03-01 10:00:02 GET /cart 500 250ms
2024-03-01 10:00:03 POST /pay 200 80ms
2024-03-01 10:00:04 GET /cart 500 310ms
bad line
2024-03-01 10:00:05 GET /home 200 8ms
"""
pat = re.compile(r"^(?P<ts>\S+ \S+) (?P<method>[A-Z]+) (?P<path>\S+) (?P<status>\d{3}) (?P<ms>\d+)ms$")
status, slow = Counter(), defaultdict(list)
bad = 0
for line in LOG.splitlines():
    m = pat.match(line)
    if not m:
        bad += 1
        continue
    status[m["status"]] += 1
    slow[m["path"]].append(int(m["ms"]))
print(dict(status), "unparsed:", bad)
print({p: round(sum(v) / len(v), 1) for p, v in sorted(slow.items())})
