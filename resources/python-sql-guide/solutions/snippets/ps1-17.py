import sqlite3
def search(con, name=None, min_age=None, order="name"):
    sql, params = ["SELECT name, age FROM users WHERE 1=1"], []
    if name:
        sql.append("AND name LIKE ?"); params.append(f"%{name}%")
    if min_age is not None:
        sql.append("AND age >= ?"); params.append(min_age)
    col = {"name": "name", "age": "age"}[order]          # allow-listed identifier
    sql.append(f"ORDER BY {col}")
    return con.execute(" ".join(sql), params).fetchall()

con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE users (name TEXT, age INTEGER)")
con.executemany("INSERT INTO users VALUES (?, ?)", [("ada", 36), ("ben", 25), ("alan", 41)])
print(search(con, name="a", min_age=30, order="age"))
print(search(con, name="x' OR '1'='1"))
