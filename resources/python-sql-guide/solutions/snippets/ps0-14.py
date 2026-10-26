import csv, io, sqlite3
from datetime import date

RAW = """order_id,customer,amount,order_date
1,Ada,120.50,2024-01-05
2,Ben,80,2024-01-07
3,Ada,,2024-02-01
4,Cy,45.25,2024-02-10
2,Ben,80,2024-01-07
5,Dev,300,not-a-date
"""

def extract(text):
    return list(csv.DictReader(io.StringIO(text)))

def transform(rows):
    seen, good, bad = set(), [], []
    for r in rows:
        try:
            if r["order_id"] in seen:
                continue                                  # drop duplicates
            amount = float(r["amount"])                   # empty string raises ValueError
            day = date.fromisoformat(r["order_date"])
            seen.add(r["order_id"])
            good.append((int(r["order_id"]), r["customer"].strip().title(), round(amount, 2), day.isoformat()))
        except ValueError as e:
            bad.append((r["order_id"], str(e)))
    return good, bad

def load(con, rows):
    con.execute("CREATE TABLE IF NOT EXISTS orders (order_id INTEGER PRIMARY KEY, customer TEXT, amount REAL, order_date TEXT)")
    with con:
        con.executemany("INSERT OR REPLACE INTO orders VALUES (?, ?, ?, ?)", rows)   # idempotent reload

good, bad = transform(extract(RAW))
con = sqlite3.connect(":memory:")
load(con, good); load(con, good)                           # running twice changes nothing
print("loaded", len(good), "rejected", len(bad))
for order_id, reason in bad:
    print("  rejected order", order_id)
print(con.execute("""SELECT customer, SUM(amount) AS total, COUNT(*) AS n
                     FROM orders GROUP BY customer ORDER BY total DESC""").fetchall())
