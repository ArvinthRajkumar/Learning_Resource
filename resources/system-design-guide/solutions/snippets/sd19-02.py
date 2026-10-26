import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("CREATE TABLE balance(acct TEXT PRIMARY KEY, amount INT); CREATE TABLE processed(msg_id TEXT PRIMARY KEY);")
db.execute("INSERT INTO balance VALUES('a', 100)")
def handle(msg_id, acct, delta):
    try:
        with db:
            db.execute("INSERT INTO processed VALUES(?)", (msg_id,))      # fails if seen
            db.execute("UPDATE balance SET amount = amount + ? WHERE acct = ?", (delta, acct))
    except sqlite3.IntegrityError:
        return "duplicate ignored"
    return "applied"
stream = [("m1", "a", 50), ("m2", "a", -30), ("m1", "a", 50), ("m2", "a", -30), ("m3", "a", 10)]   # duplicates delivered
print([handle(*m) for m in stream])
print("balance:", db.execute("SELECT amount FROM balance").fetchone()[0], "(expected 100 + 50 - 30 + 10 = 130)")
