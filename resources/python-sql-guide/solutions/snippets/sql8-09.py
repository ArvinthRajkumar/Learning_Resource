import sqlite3
db = sqlite3.connect(":memory:", isolation_level=None)
db.executescript("CREATE TABLE payment(request_id TEXT PRIMARY KEY, amount INT); CREATE TABLE ledger(total INT); INSERT INTO ledger VALUES (0);")
def pay(request_id, amount):
    db.execute("BEGIN")
    cur = db.execute("INSERT INTO payment VALUES (?, ?) ON CONFLICT(request_id) DO NOTHING", (request_id, amount))
    if cur.rowcount == 1:
        db.execute("UPDATE ledger SET total = total + ?", (amount,))
    db.execute("COMMIT")
    return "applied" if cur.rowcount == 1 else "duplicate ignored"
print([pay("req-1", 50), pay("req-1", 50), pay("req-2", 20), pay("req-1", 50)])
print("ledger total:", db.execute("SELECT total FROM ledger").fetchone()[0], "(70, not 170)")
