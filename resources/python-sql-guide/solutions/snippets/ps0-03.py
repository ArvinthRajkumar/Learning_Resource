import sqlite3, datetime, json
con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE ev (at TEXT, payload TEXT)")
now = datetime.datetime(2024, 3, 5, 12, 0, tzinfo=datetime.timezone.utc)
con.execute("INSERT INTO ev VALUES (?, ?)", (now.isoformat(), json.dumps({"k": [1, 2]})))
at, payload = con.execute("SELECT at, payload FROM ev").fetchone()
print(datetime.datetime.fromisoformat(at).year, json.loads(payload)["k"])
