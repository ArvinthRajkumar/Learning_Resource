import sqlite3
MIGRATIONS = [
    (1, "create users",       "CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT NOT NULL UNIQUE)"),
    (2, "add display name",   "ALTER TABLE users ADD COLUMN display_name TEXT"),
    (3, "create orders",      "CREATE TABLE orders (id INTEGER PRIMARY KEY, user_id INTEGER NOT NULL REFERENCES users(id), total_cents INTEGER NOT NULL)"),
    (4, "index orders.user",  "CREATE INDEX idx_orders_user ON orders(user_id)"),
]
def migrate(db, migrations):
    db.execute("CREATE TABLE IF NOT EXISTS schema_migrations (version INTEGER PRIMARY KEY, name TEXT, applied_at TEXT DEFAULT CURRENT_TIMESTAMP)")
    done = {v for (v,) in db.execute("SELECT version FROM schema_migrations")}
    applied = []
    for version, name, sql in sorted(migrations):
        if version in done: continue
        db.execute("BEGIN")
        try:
            db.execute(sql)
            db.execute("INSERT INTO schema_migrations(version, name) VALUES (?, ?)", (version, name))
            db.execute("COMMIT"); applied.append(version)
        except sqlite3.Error:
            db.execute("ROLLBACK"); raise
    return applied
db = sqlite3.connect(":memory:", isolation_level=None)
print("first run applies:", migrate(db, MIGRATIONS))
print("second run applies:", migrate(db, MIGRATIONS))
print("columns of users:", [r[1] for r in db.execute("PRAGMA table_info(users)")])
print("recorded versions:", [r[0] for r in db.execute("SELECT version FROM schema_migrations ORDER BY version")])
MIGRATIONS.append((5, "bad migration", "ALTER TABLE nonexistent ADD COLUMN x INT"))
try: migrate(db, MIGRATIONS)
except sqlite3.Error as e: print("migration 5 failed and was rolled back:", e)
print("versions after failure:", [r[0] for r in db.execute("SELECT version FROM schema_migrations ORDER BY version")])
