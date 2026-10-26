import sqlite3, os, tempfile
path = os.path.join(tempfile.mkdtemp(), "demo.db")
a = sqlite3.connect(path, isolation_level=None, timeout=0.2)
b = sqlite3.connect(path, isolation_level=None, timeout=0.2)
a.execute("CREATE TABLE t(id INTEGER PRIMARY KEY, v INT)"); a.execute("INSERT INTO t VALUES (1, 10)")
a.execute("BEGIN IMMEDIATE")                                  # A takes the write lock
a.execute("UPDATE t SET v = 20 WHERE id = 1")
try:
    b.execute("BEGIN IMMEDIATE")                              # B also wants to write
    b.execute("UPDATE t SET v = 99 WHERE id = 1")
except sqlite3.OperationalError as e:
    print("B is blocked:", e)
a.execute("COMMIT")
b.execute("BEGIN IMMEDIATE"); b.execute("UPDATE t SET v = v + 1 WHERE id = 1"); b.execute("COMMIT")
print("after both finish:", a.execute("SELECT v FROM t").fetchone()[0])
