import csv, io, sqlite3
data = "region,product,units\nEU,pen,10\nEU,book,3\nUS,pen,7\nUS,pen,5\nUS,book,9\n"
con = sqlite3.connect(":memory:")
con.execute("CREATE TABLE sales (region TEXT, product TEXT, units INTEGER)")
rows = [(r["region"], r["product"], int(r["units"])) for r in csv.DictReader(io.StringIO(data))]
with con:
    con.executemany("INSERT INTO sales VALUES (?, ?, ?)", rows)
q = """
SELECT region, product, SUM(units) AS total,
       RANK() OVER (PARTITION BY region ORDER BY SUM(units) DESC) AS rnk
FROM sales GROUP BY region, product ORDER BY region, rnk
"""
for row in con.execute(q):
    print(row)
