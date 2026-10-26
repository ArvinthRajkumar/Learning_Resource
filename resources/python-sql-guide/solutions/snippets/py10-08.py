from datetime import date, timedelta
from collections import Counter
events = ["2024-03-01", "2024-03-01", "2024-03-03", "2024-03-06", "2024-03-06", "2024-03-06"]
counts = Counter(date.fromisoformat(e) for e in events)
start, end = min(counts), max(counts)
series = [(start + timedelta(days=i), counts.get(start + timedelta(days=i), 0)) for i in range((end - start).days + 1)]   # fill gaps with 0
print([(d.isoformat()[5:], n) for d, n in series])
window = 3
print("3-day moving sum:", [sum(n for _, n in series[max(0, i - window + 1): i + 1]) for i in range(len(series))])
weekly = Counter((d - timedelta(days=d.weekday())).isoformat() for d in (date.fromisoformat(e) for e in events))
print("per ISO week (week start):", dict(weekly))
