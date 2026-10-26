import sqlite3
from contextlib import closing
with closing(sqlite3.connect(":memory:")) as con, con:      # closes the connection AND commits
    con.execute("CREATE TABLE x (v INTEGER)")
    con.execute("INSERT INTO x VALUES (1)")
    print(con.execute("SELECT * FROM x").fetchall())
