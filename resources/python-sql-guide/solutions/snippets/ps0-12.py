import sqlite3
MIGRATIONS = [
    ("001_create_users", "CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT NOT NULL)"),
    ("002_add_email", "ALTER TABLE users ADD COLUMN email TEXT"),
    ("003_email_index", "CREATE INDEX idx_users_email ON users(email)"),
]

def migrate(con):
    con.execute("CREATE TABLE IF NOT EXISTS schema_migrations (version TEXT PRIMARY KEY)")
    done = {v for (v,) in con.execute("SELECT version FROM schema_migrations")}
    for version, sql in MIGRATIONS:
        if version not in done:
            with con:
                con.execute(sql)
                con.execute("INSERT INTO schema_migrations VALUES (?)", (version,))
            print("applied", version)

con = sqlite3.connect(":memory:")
migrate(con)
migrate(con)                       # second run applies nothing: idempotent
print([r[0] for r in con.execute("SELECT version FROM schema_migrations ORDER BY version")])
