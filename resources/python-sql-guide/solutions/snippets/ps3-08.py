import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("CREATE TABLE author(id INT, name TEXT); CREATE TABLE book(id INT, author_id INT, title TEXT);"
                 "INSERT INTO author VALUES (1,'a'),(2,'b'),(3,'c'); INSERT INTO book VALUES (1,1,'x'),(2,1,'y'),(3,2,'z'),(4,3,'w');")
queries = 0
authors = db.execute("SELECT id, name FROM author").fetchall(); queries += 1
for aid, name in authors:                                               # N more queries, one per author
    db.execute("SELECT title FROM book WHERE author_id = ?", (aid,)).fetchall(); queries += 1
print("queries with the N+1 pattern for 3 authors:", queries)
joined = db.execute("SELECT a.name, b.title FROM author a JOIN book b ON b.author_id = a.id").fetchall()
print("queries with one join:", 1, "| rows:", len(joined))
