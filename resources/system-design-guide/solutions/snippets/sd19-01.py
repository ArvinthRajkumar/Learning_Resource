import sqlite3, json
db = sqlite3.connect(":memory:")
db.executescript("""CREATE TABLE orders(id INTEGER PRIMARY KEY, item TEXT, qty INT);
                     CREATE TABLE outbox(id INTEGER PRIMARY KEY AUTOINCREMENT, topic TEXT, payload TEXT, sent INT DEFAULT 0);""")
def place_order(order_id, item, qty, fail=False):
    try:
        with db:                                   # one atomic transaction
            db.execute("INSERT INTO orders VALUES(?,?,?)", (order_id, item, qty))
            db.execute("INSERT INTO outbox(topic, payload) VALUES('order.placed', ?)", (json.dumps({"id": order_id, "item": item, "qty": qty}),))
            if fail: raise RuntimeError("crash before commit")
    except RuntimeError:
        pass
place_order(1, "book", 2)
place_order(2, "pen", 5, fail=True)               # rolled back: no order AND no event
print("orders:", db.execute("SELECT id FROM orders").fetchall(), "| outbox:", db.execute("SELECT id, topic FROM outbox").fetchall())
broker = []
for rid, topic, payload in db.execute("SELECT id, topic, payload FROM outbox WHERE sent = 0").fetchall():
    broker.append((topic, payload))                # relay publishes ...
    db.execute("UPDATE outbox SET sent = 1 WHERE id = ?", (rid,))   # ... then marks sent (crash in between = duplicate)
db.commit()
print("published:", broker)
