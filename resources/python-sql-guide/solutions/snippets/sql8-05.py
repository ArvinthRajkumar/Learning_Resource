import sqlite3, os, tempfile
path = os.path.join(tempfile.mkdtemp(), "wal.db")
w = sqlite3.connect(path, isolation_level=None)
r = sqlite3.connect(path, isolation_level=None)
print("journal mode:", w.execute("PRAGMA journal_mode=WAL").fetchone()[0])
w.execute("CREATE TABLE t(id INTEGER PRIMARY KEY, v INT)"); w.execute("INSERT INTO t VALUES (1, 10)")
r.execute("BEGIN"); first = r.execute("SELECT v FROM t WHERE id = 1").fetchone()[0]     # snapshot starts here
w.execute("UPDATE t SET v = 20 WHERE id = 1")                                          # committed by the writer
second = r.execute("SELECT v FROM t WHERE id = 1").fetchone()[0]                       # still the old snapshot
r.execute("COMMIT")
third = r.execute("SELECT v FROM t WHERE id = 1").fetchone()[0]                        # new transaction sees new data
print("reader saw", first, "then", second, "inside its transaction, and", third, "afterwards")
