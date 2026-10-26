import sqlite3
con = sqlite3.connect(":memory:")
con.executescript("""
CREATE TABLE author (id INTEGER PRIMARY KEY, name TEXT);
CREATE TABLE book (id INTEGER PRIMARY KEY, author_id INTEGER, title TEXT);
INSERT INTO author VALUES (1,'Ada'),(2,'Ben'),(3,'Cy');
INSERT INTO book VALUES (1,1,'A1'),(2,1,'A2'),(3,2,'B1'),(4,3,'C1'),(5,3,'C2');
""")
count = [0]
con.set_trace_callback(lambda sql: count.__setitem__(0, count[0] + 1))

# N+1: one query for authors, then one per author
for a_id, name in con.execute("SELECT id, name FROM author").fetchall():
    con.execute("SELECT title FROM book WHERE author_id = ?", (a_id,)).fetchall()
print("N+1 queries:", count[0])

count[0] = 0
rows = con.execute("SELECT a.name, b.title FROM author a JOIN book b ON b.author_id = a.id").fetchall()
print("single join queries:", count[0], len(rows), "rows")
