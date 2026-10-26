import csv, io
raw = 'id,name,city,amount\n1,"Smith, Ana",London,10.5\n2,Bo,"Paris\nFrance",\n3,Chloe,,7\n'
rows = list(csv.DictReader(io.StringIO(raw)))
for r in rows: print(r)
total = sum(float(r["amount"]) for r in rows if r["amount"])
print("total:", total, "| rows with missing amount:", [r["id"] for r in rows if not r["amount"]])
out = io.StringIO()
w = csv.DictWriter(out, fieldnames=["id", "name"], extrasaction="ignore", lineterminator="\n")
w.writeheader(); w.writerows(rows)
print(out.getvalue().strip().replace("\n", " / "))
