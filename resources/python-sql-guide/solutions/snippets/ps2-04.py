import sqlite3
ALLOWED_COLUMNS = {"name", "city", "age"}
ALLOWED_OPS = {"eq": "=", "lt": "<", "gt": ">", "like": "LIKE"}
ALLOWED_SORT = {"name", "age"}
def build_query(filters, sort=None, limit=10):
    sql, params = "SELECT id, name, city, age FROM person", []
    clauses = []
    for col, op, value in filters:
        if col not in ALLOWED_COLUMNS or op not in ALLOWED_OPS: raise ValueError(f"filter not allowed: {col} {op}")
        clauses.append(f"{col} {ALLOWED_OPS[op]} ?"); params.append(value)
    if clauses: sql += " WHERE " + " AND ".join(clauses)
    if sort:
        col, _, direction = sort.partition(" ")
        if col not in ALLOWED_SORT or direction.upper() not in ("", "ASC", "DESC"): raise ValueError("sort not allowed")
        sql += f" ORDER BY {col} {direction.upper() or 'ASC'}"
    sql += " LIMIT ?"; params.append(max(1, min(int(limit), 100)))
    return sql, params
db = sqlite3.connect(":memory:")
db.executescript("CREATE TABLE person (id INTEGER PRIMARY KEY, name TEXT, city TEXT, age INT); INSERT INTO person VALUES (1,'Ana','Pune',30),(2,'Bo','Pune',22),(3,'Cy','Goa',41),(4,'Di','Goa',35);")
sql, params = build_query([("city", "eq", "Goa"), ("age", "gt", 30)], sort="age desc")
print(sql, params)
print(db.execute(sql, params).fetchall())
for evil in [[("name; DROP TABLE person; --", "eq", "x")], [("name", "eq or 1=1", "x")]]:
    try: build_query(evil)
    except ValueError as e: print("blocked:", e)
print("injection attempt as a VALUE is just data:", db.execute(*build_query([("name", "eq", "x' OR '1'='1")])).fetchall())
