import sqlite3
db = sqlite3.connect(":memory:", isolation_level=None)
db.execute("CREATE TABLE inventory(sku TEXT PRIMARY KEY, available INT)")
db.execute("INSERT INTO inventory VALUES('phone', 1)")
# Racy read-modify-write, with the two buyers' steps interleaved exactly as concurrent requests can interleave
a_read = db.execute("SELECT available FROM inventory").fetchone()[0]       # buyer A reads 1
b_read = db.execute("SELECT available FROM inventory").fetchone()[0]       # buyer B reads 1
db.execute("UPDATE inventory SET available = ?", (a_read - 1,))            # A writes 0 and succeeds
db.execute("UPDATE inventory SET available = ?", (b_read - 1,))            # B also writes 0 and succeeds
print("read-then-write: both buyers think they bought the last phone (A saw", a_read, ", B saw", b_read, ")")
db.execute("UPDATE inventory SET available = 1")
wins = []
for buyer in ("A", "B"):                                                   # same two buyers, atomic conditional update
    cur = db.execute("UPDATE inventory SET available = available - 1 WHERE sku = 'phone' AND available > 0")
    wins.append((buyer, cur.rowcount == 1))
print("atomic conditional update:", wins, "| stock left:", db.execute("SELECT available FROM inventory").fetchone()[0])
