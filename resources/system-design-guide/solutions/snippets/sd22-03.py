import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("CREATE TABLE users(name TEXT, secret TEXT); INSERT INTO users VALUES('ana','a-secret'),('bo','b-secret');")
evil = "x' OR '1'='1"
unsafe = db.execute(f"SELECT name FROM users WHERE name = '{evil}'").fetchall()          # string building
safe = db.execute("SELECT name FROM users WHERE name = ?", (evil,)).fetchall()           # parameter binding
print("injected query returns:", unsafe, "| parameterised query returns:", safe)
