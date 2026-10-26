from datetime import datetime, timezone
import calendar
print("days in Feb 2024:", calendar.monthrange(2024, 2)[1], "| leap 2100?", calendar.isleap(2100))
naive, aware = datetime(2024, 1, 1), datetime(2024, 1, 1, tzinfo=timezone.utc)
try:
    naive < aware
except TypeError as e:
    print("mixing naive and aware fails:", e)
