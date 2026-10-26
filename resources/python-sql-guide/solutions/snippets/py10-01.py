rows = [
    {"order": 1, "customer": "ana", "country": "IN", "amount": 120.0, "date": "2024-03-01"},
    {"order": 2, "customer": "bo",  "country": "US", "amount": 80.5,  "date": "2024-03-02"},
    {"order": 3, "customer": "ana", "country": "IN", "amount": 45.0,  "date": "2024-03-05"},
    {"order": 4, "customer": "cy",  "country": "DE", "amount": None,  "date": "2024-03-05"},
    {"order": 5, "customer": "bo",  "country": "US", "amount": 200.0, "date": "2024-03-09"},
]
columns = {k: [r[k] for r in rows] for k in rows[0]}              # rows -> columns (a "transpose")
print(columns["amount"])
back = [dict(zip(columns, vals)) for vals in zip(*columns.values())]     # columns -> rows
print(back == rows)
