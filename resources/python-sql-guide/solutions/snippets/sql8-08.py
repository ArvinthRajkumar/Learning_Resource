import sqlite3
db = sqlite3.connect(":memory:", isolation_level=None)
db.executescript("CREATE TABLE item(id INTEGER PRIMARY KEY, name TEXT UNIQUE);")
db.execute("BEGIN")
db.execute("INSERT INTO item(name) VALUES ('a')")
db.execute("SAVEPOINT sp1")
try:
    db.execute("INSERT INTO item(name) VALUES ('a')")          # duplicate: violates UNIQUE
except sqlite3.IntegrityError as e:
    db.execute("ROLLBACK TO sp1")                              # undo only the failed part
    print("duplicate rejected, transaction continues:", e)
db.execute("INSERT INTO item(name) VALUES ('b')")
db.execute("COMMIT")
print(db.execute("SELECT name FROM item ORDER BY name").fetchall())
