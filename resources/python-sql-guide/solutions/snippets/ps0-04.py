import sqlite3
con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE users (name TEXT, secret TEXT)")
con.execute("INSERT INTO users VALUES ('ada', 's3cret'), ('ben', 'hunter2')")

user_input = "nobody' OR '1'='1"

unsafe = "SELECT name, secret FROM users WHERE name = '%s'" % user_input
print("UNSAFE query text:", unsafe)
print("unsafe rows leaked:", con.execute(unsafe).fetchall())

safe_rows = con.execute("SELECT name, secret FROM users WHERE name = ?", (user_input,)).fetchall()
print("safe rows:", safe_rows)
