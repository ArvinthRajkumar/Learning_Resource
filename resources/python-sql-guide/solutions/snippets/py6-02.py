from datetime import date, datetime, timedelta, timezone
d = date(2024, 1, 31)
print("weekday (Mon=0):", d.weekday(), "| iso:", d.isoformat(), "| +30 days:", d + timedelta(days=30))
a, b = datetime(2024, 3, 1, 9, 0), datetime(2024, 3, 3, 17, 30)
delta = b - a
print("difference:", delta, "| total hours:", delta.total_seconds() / 3600)
print("parsed:", datetime.strptime("25/12/2024 18:45", "%d/%m/%Y %H:%M"), "| formatted:", a.strftime("%A, %d %B %Y"))
utc = datetime(2024, 7, 1, 12, 0, tzinfo=timezone.utc)
ist = utc.astimezone(timezone(timedelta(hours=5, minutes=30), "IST"))
print("UTC:", utc.isoformat(), "| fixed-offset IST:", ist.isoformat())
