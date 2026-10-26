import csv, io
buf = io.StringIO()
w = csv.writer(buf)
w.writerow(["name", "city"])
w.writerows([["Ada", "London"], ["Ben", "Paris, FR"]])
text = buf.getvalue()
print(text)
for row in csv.DictReader(io.StringIO(text)):
    print(row["name"], "|", row["city"])
