import sqlite3, time
db = sqlite3.connect(":memory:")
db.execute("CREATE TABLE seats (id INTEGER PRIMARY KEY, status TEXT, held_by TEXT, hold_until REAL)")
db.execute("INSERT INTO seats VALUES (1, 'available', NULL, NULL)")

def hold(seat, user, now, ttl=600):
    # one atomic statement: succeeds only if the seat is available or its hold expired
    cur = db.execute("""UPDATE seats SET status='held', held_by=?, hold_until=?
                        WHERE id=? AND (status='available' OR (status='held' AND hold_until < ?))""",
                     (user, now + ttl, seat, now))
    return cur.rowcount == 1

print("alice:", hold(1, "alice", now=0))
print("bob  :", hold(1, "bob", now=100))        # still held by alice
print("bob after expiry:", hold(1, "bob", now=700))
