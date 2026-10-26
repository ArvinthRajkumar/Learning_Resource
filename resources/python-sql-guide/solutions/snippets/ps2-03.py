import sqlite3
db = sqlite3.connect(":memory:", isolation_level=None)
db.executescript("""
CREATE TABLE customer (id INTEGER PRIMARY KEY, email TEXT, country TEXT, created TEXT);
CREATE TABLE orders (id INTEGER PRIMARY KEY, customer_id INT, total REAL, status TEXT, placed TEXT);
INSERT INTO customer VALUES (1,'a@x.com','US','2024-01-01'),(2,'b@x.com','DE','2024-01-02'),(3,NULL,'US','2024-01-03'),(4,'a@x.com','FR','2024-01-04');
INSERT INTO orders VALUES (1,1,50,'paid','2024-02-01'),(2,2,-5,'paid','2024-02-02'),(3,99,20,'paid','2024-02-03'),(4,1,10,'weird','2024-02-04'),(5,2,15,'paid','2099-01-01');
""")
CHECKS = [
    ("customer emails not null",      "SELECT id FROM customer WHERE email IS NULL"),
    ("customer emails unique",        "SELECT email FROM customer WHERE email IS NOT NULL GROUP BY email HAVING COUNT(*) > 1"),
    ("order totals positive",         "SELECT id FROM orders WHERE total <= 0"),
    ("orders reference customers",    "SELECT o.id FROM orders o LEFT JOIN customer c ON c.id = o.customer_id WHERE c.id IS NULL"),
    ("order status in allowed set",   "SELECT id FROM orders WHERE status NOT IN ('paid','pending','cancelled')"),
    ("no orders dated in the future", "SELECT id FROM orders WHERE placed > date('2024-12-31')"),
]
def run_checks(db, checks):
    results = []
    for name, sql in checks:
        bad = [r[0] for r in db.execute(sql)]
        results.append((name, "PASS" if not bad else "FAIL", bad))
    return results
for name, status, bad in run_checks(db, CHECKS):
    print(f"{status}  {name}" + (f"  -> offending: {bad}" if bad else ""))
