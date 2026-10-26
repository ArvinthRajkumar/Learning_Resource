import sqlite3
db = sqlite3.connect(":memory:", isolation_level=None)
db.executescript("CREATE TABLE acct(id INTEGER PRIMARY KEY, bal INT CHECK (bal >= 0)); INSERT INTO acct VALUES (1, 100), (2, 50);")
def transfer(src, dst, amount):
    db.execute("BEGIN")
    try:
        db.execute("UPDATE acct SET bal = bal - ? WHERE id = ?", (amount, src))   # may violate CHECK
        db.execute("UPDATE acct SET bal = bal + ? WHERE id = ?", (amount, dst))
        db.execute("COMMIT"); return "committed"
    except sqlite3.Error as e:
        db.execute("ROLLBACK"); return f"rolled back ({e})"
print(transfer(1, 2, 30))
print(transfer(1, 2, 500))
print("balances:", db.execute("SELECT id, bal FROM acct ORDER BY id").fetchall(), "| total is still", db.execute("SELECT SUM(bal) FROM acct").fetchone()[0])
