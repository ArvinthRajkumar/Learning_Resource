import sqlite3
db = sqlite3.connect(":memory:", isolation_level=None)
db.executescript("CREATE TABLE counter(id INTEGER PRIMARY KEY, n INT); INSERT INTO counter VALUES (1, 10);")
a = db.execute("SELECT n FROM counter WHERE id = 1").fetchone()[0]          # session A reads 10
b = db.execute("SELECT n FROM counter WHERE id = 1").fetchone()[0]          # session B reads 10
db.execute("UPDATE counter SET n = ? WHERE id = 1", (a + 1,))               # A writes 11
db.execute("UPDATE counter SET n = ? WHERE id = 1", (b + 1,))               # B writes 11 (A's update is lost)
print("read-modify-write result:", db.execute("SELECT n FROM counter").fetchone()[0], "(two increments, but the value went up by one)")
db.execute("UPDATE counter SET n = 10")
db.execute("UPDATE counter SET n = n + 1 WHERE id = 1")                      # atomic, evaluated inside the database
db.execute("UPDATE counter SET n = n + 1 WHERE id = 1")
print("atomic increment result :", db.execute("SELECT n FROM counter").fetchone()[0])
