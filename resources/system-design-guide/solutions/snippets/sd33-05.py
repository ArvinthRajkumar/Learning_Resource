import sqlite3
db = sqlite3.connect(":memory:")
db.executescript("""
CREATE TABLE node (id INTEGER PRIMARY KEY, name TEXT, parent_id INT, path TEXT);
INSERT INTO node VALUES (1,'Electronics',NULL,'/1/'),(2,'Phones',1,'/1/2/'),(3,'Laptops',1,'/1/3/'),(4,'Gaming laptops',3,'/1/3/4/'),(5,'Clothing',NULL,'/5/');
CREATE INDEX idx_path ON node(path);
""")
print("subtree of Electronics by path prefix:", [r[0] for r in db.execute("SELECT name FROM node WHERE path LIKE '/1/%' ORDER BY path")])
rec = db.execute("""WITH RECURSIVE sub(id, name) AS (SELECT id, name FROM node WHERE id = 3 UNION ALL SELECT n.id, n.name FROM node n JOIN sub s ON n.parent_id = s.id) SELECT name FROM sub""").fetchall()
print("subtree of Laptops by recursive CTE:", [r[0] for r in rec])
