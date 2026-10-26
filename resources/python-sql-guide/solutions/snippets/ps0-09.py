import sqlite3, time
rows = [(i, f"user{i}") for i in range(20000)]

def one_by_one():
    con = sqlite3.connect(":memory:")
    con.execute("CREATE TABLE u (id INTEGER, name TEXT)")
    for r in rows[:2000]:
        con.execute("INSERT INTO u VALUES (?, ?)", r)
        con.commit()                                   # commit per row: slow on a real disk
    return time.perf_counter()

def bulk():
    con = sqlite3.connect(":memory:")
    con.execute("CREATE TABLE u (id INTEGER, name TEXT)")
    with con:
        con.executemany("INSERT INTO u VALUES (?, ?)", rows)
    return con.execute("SELECT COUNT(*) FROM u").fetchone()[0]

print(bulk(), "rows inserted with executemany")
