import sqlite3

con = sqlite3.connect(":memory:")            # a database held in memory (use a filename for a file)
cur = con.cursor()
cur.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL, age INTEGER)")
cur.execute("INSERT INTO users (name, age) VALUES (?, ?)", ("Ada", 36))
cur.executemany("INSERT INTO users (name, age) VALUES (?, ?)", [("Ben", 25), ("Cy", 41)])
con.commit()

cur.execute("SELECT id, name, age FROM users WHERE age > ? ORDER BY age", (30,))
print(cur.fetchall())
print(cur.description[0][0], "|", cur.rowcount)
cur.execute("SELECT COUNT(*) FROM users")
print(cur.fetchone()[0])
con.close()
