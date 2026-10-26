import sqlite3
con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE acct (name TEXT PRIMARY KEY, bal INTEGER NOT NULL CHECK (bal >= 0))")
con.executemany("INSERT INTO acct VALUES (?, ?)", [("alice", 100), ("bob", 20)])
con.commit()

def transfer(src, dst, amount):
    with con:                                        # one transaction
        con.execute("UPDATE acct SET bal = bal - ? WHERE name = ?", (amount, src))
        con.execute("UPDATE acct SET bal = bal + ? WHERE name = ?", (amount, dst))

transfer("alice", "bob", 30)
print(con.execute("SELECT * FROM acct ORDER BY name").fetchall())
try:
    transfer("alice", "bob", 500)                     # violates CHECK, whole transaction rolls back
except sqlite3.IntegrityError as e:
    print("failed:", e)
print(con.execute("SELECT * FROM acct ORDER BY name").fetchall())
