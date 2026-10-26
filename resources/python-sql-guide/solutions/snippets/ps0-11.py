import sqlite3
con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE big (n INTEGER)")
con.executemany("INSERT INTO big VALUES (?)", ((i,) for i in range(100000)))
total = 0
for (n,) in con.execute("SELECT n FROM big"):            # iterates lazily instead of fetchall()
    total += n
print(total)
cur = con.execute("SELECT n FROM big ORDER BY n")
while batch := cur.fetchmany(25000):
    print(len(batch), batch[0][0])
