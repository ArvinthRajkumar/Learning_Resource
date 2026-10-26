import sqlite3
con = sqlite3.connect(":memory:")
con.row_factory = sqlite3.Row                 # rows behave like dicts and tuples
con.execute("CREATE TABLE t (a INTEGER, b TEXT)")
con.execute("INSERT INTO t VALUES (1, 'x'), (2, 'y')")
for row in con.execute("SELECT a, b FROM t ORDER BY a"):
    print(row["a"], row["b"], tuple(row), dict(row))
