import sqlite3
con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE t (a INTEGER, b TEXT)")
con.execute("INSERT INTO t VALUES (:a, :b)", {"a": 1, "b": "one"})
ids = [1, 2, 3]
placeholders = ", ".join("?" * len(ids))          # build placeholders, not values
print(con.execute(f"SELECT {placeholders} AS expanded", ids).fetchall())
