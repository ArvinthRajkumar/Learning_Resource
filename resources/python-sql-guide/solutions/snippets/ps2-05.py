import json, sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE sale (id INTEGER PRIMARY KEY, region TEXT, product TEXT, qty INT, unit_cents INT, day TEXT);
INSERT INTO sale VALUES
 (1,'north','pen',10,150,'2024-05-01'),(2,'north','book',2,1200,'2024-05-02'),(3,'south','pen',30,140,'2024-05-02'),
 (4,'south','book',5,1250,'2024-05-03'),(5,'north','pen',5,150,'2024-05-04'),(6,'east','lamp',1,3500,'2024-05-04');
""")
def sales_summary(db, group_by="region"):
    assert group_by in {"region", "product"}                       # allow-list the identifier
    rows = db.execute(f"SELECT {group_by}, SUM(qty * unit_cents), SUM(qty) FROM sale GROUP BY {group_by} ORDER BY SUM(qty * unit_cents) DESC").fetchall()
    total = sum(r[1] for r in rows)
    return {"group_by": group_by, "total": total / 100,
            "rows": [{"key": k, "revenue": c / 100, "units": q, "share": round(c / total, 3)} for k, c, q in rows]}
def handle(path):
    """A framework-free 'route': returns (status, json body)."""
    if path.startswith("/summary/"):
        try: return 200, json.dumps(sales_summary(db, path.split("/")[-1]))
        except AssertionError: return 400, json.dumps({"error": "group_by must be region or product"})
    return 404, json.dumps({"error": "not found"})
status, body = handle("/summary/region")
payload = json.loads(body)
print(status, payload["group_by"], payload["total"])
for row in payload["rows"]: print(row)
print(handle("/summary/customer")); print(handle("/nope"))
