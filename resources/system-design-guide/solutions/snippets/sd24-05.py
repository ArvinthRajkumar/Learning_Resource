import sqlite3
db = sqlite3.connect(":memory:", isolation_level=None)
db.executescript("""CREATE TABLE inv(room_type TEXT, night INT, total INT, reserved INT, PRIMARY KEY(room_type, night));
                    CREATE TABLE res(id INTEGER PRIMARY KEY AUTOINCREMENT, room_type TEXT, start INT, end INT);""")
for n in range(1, 8): db.execute("INSERT INTO inv VALUES('double', ?, 2, 0)", (n,))
def book(room_type, start, end):
    db.execute("BEGIN IMMEDIATE")
    nights = (end - start)
    ok = db.execute("SELECT COUNT(*) FROM inv WHERE room_type=? AND night>=? AND night<? AND reserved < total", (room_type, start, end)).fetchone()[0] == nights
    if not ok:
        db.execute("ROLLBACK"); return False
    db.execute("UPDATE inv SET reserved = reserved + 1 WHERE room_type=? AND night>=? AND night<?", (room_type, start, end))
    db.execute("INSERT INTO res(room_type, start, end) VALUES(?,?,?)", (room_type, start, end))
    db.execute("COMMIT"); return True
print([book("double", 2, 5), book("double", 3, 6), book("double", 4, 7), book("double", 1, 3), book("double", 5, 7)])
print("reserved per night:", db.execute("SELECT night, reserved FROM inv ORDER BY night").fetchall())
