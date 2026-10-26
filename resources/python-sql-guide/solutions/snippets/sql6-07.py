import json, sqlite3
# Relational: three tables joined at read time
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE orders(id INTEGER PRIMARY KEY, customer TEXT);
CREATE TABLE lines(order_id INT, sku TEXT, qty INT, price REAL);
INSERT INTO orders VALUES (1, 'ana');
INSERT INTO lines VALUES (1, 'pen', 3, 2.0), (1, 'book', 1, 15.0);""")
rel = db.execute("SELECT o.id, o.customer, SUM(l.qty * l.price) FROM orders o JOIN lines l ON l.order_id = o.id GROUP BY o.id").fetchone()
# Document: the order is one self-contained document, read in a single lookup
doc = {"_id": 1, "customer": "ana", "lines": [{"sku": "pen", "qty": 3, "price": 2.0}, {"sku": "book", "qty": 1, "price": 15.0}]}
total = sum(l["qty"] * l["price"] for l in doc["lines"])
print("relational result:", rel)
print("document total   :", (doc["_id"], doc["customer"], total))
print("document as stored:", json.dumps(doc))
