import sqlite3
db = sqlite3.connect(":memory:", isolation_level=None)
db.executescript("CREATE TABLE doc(id INTEGER PRIMARY KEY, body TEXT, version INT); INSERT INTO doc VALUES (1, 'v1 text', 1);")
def load(): return db.execute("SELECT body, version FROM doc WHERE id = 1").fetchone()
def save(body, expected_version):
    cur = db.execute("UPDATE doc SET body = ?, version = version + 1 WHERE id = 1 AND version = ?", (body, expected_version))
    return cur.rowcount == 1
body_a, ver_a = load()          # editor A opens the document
body_b, ver_b = load()          # editor B opens the same version
print("A saves:", save("edited by A", ver_a))
print("B saves with a stale version:", save("edited by B", ver_b), "-> B must reload and merge")
print("stored:", load())
