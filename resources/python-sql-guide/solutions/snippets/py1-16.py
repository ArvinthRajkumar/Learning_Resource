from datetime import date, datetime, timedelta, timezone
d = date(2024, 3, 5)
print(d.weekday(), d.isoformat(), d + timedelta(days=30))
dt = datetime(2024, 3, 5, 14, 30, tzinfo=timezone.utc)
print(dt.strftime("%Y-%m-%d %H:%M"), dt.astimezone(timezone(timedelta(hours=5, minutes=30))).isoformat())
print(datetime.fromisoformat("2024-03-05T10:00:00") - datetime(2024, 3, 1))
print((date(2024, 12, 25) - date(2024, 3, 5)).days)
