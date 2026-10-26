import sqlite3
db = sqlite3.connect(":memory:", isolation_level=None)
db.executescript("CREATE TABLE oncall(doc TEXT PRIMARY KEY, on_duty INT); INSERT INTO oncall VALUES ('ana', 1), ('bo', 1);")
# Both transactions evaluate their check against the same snapshot (state at start), then write different rows
others_for_ana = db.execute("SELECT COUNT(*) FROM oncall WHERE on_duty = 1 AND doc <> 'ana'").fetchone()[0]
others_for_bo = db.execute("SELECT COUNT(*) FROM oncall WHERE on_duty = 1 AND doc <> 'bo'").fetchone()[0]
if others_for_ana >= 1: db.execute("UPDATE oncall SET on_duty = 0 WHERE doc = 'ana'")
if others_for_bo >= 1: db.execute("UPDATE oncall SET on_duty = 0 WHERE doc = 'bo'")
print("doctors on duty afterwards:", db.execute("SELECT COUNT(*) FROM oncall WHERE on_duty = 1").fetchone()[0], "(the invariant 'at least one' is broken)")
