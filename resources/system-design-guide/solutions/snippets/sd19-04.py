events = [
    {"type": "OrderPlaced", "order": 1, "customer": "ana", "total": 40},
    {"type": "OrderPlaced", "order": 2, "customer": "bo", "total": 15},
    {"type": "OrderPlaced", "order": 3, "customer": "ana", "total": 25},
    {"type": "OrderCancelled", "order": 2},
]
spend, status = {}, {}
for e in events:                                   # one projector builds two read models
    if e["type"] == "OrderPlaced":
        spend[e["customer"]] = spend.get(e["customer"], 0) + e["total"]
        status[e["order"]] = ("placed", e["customer"], e["total"])
    elif e["type"] == "OrderCancelled":
        _, cust, tot = status[e["order"]]
        spend[cust] -= tot
        status[e["order"]] = ("cancelled", cust, tot)
print("spend per customer:", spend)
print("order status:", status)
