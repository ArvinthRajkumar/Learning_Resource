import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("CREATE TABLE u(name TEXT, pw TEXT); INSERT INTO u VALUES ('ana','s3cret');")
evil = "nobody' OR '1'='1"
print("concatenated :", db.execute("SELECT name FROM u WHERE name = '" + evil + "'").fetchall())
print("parameterised:", db.execute("SELECT name FROM u WHERE name = ?", (evil,)).fetchall())
