customers = [{"id": 1, "name": "ana", "tier": "gold"}, {"id": 2, "name": "bo", "tier": "silver"}, {"id": 3, "name": "cy", "tier": "silver"}]
orders = [{"order": 10, "cust": 1, "amount": 50}, {"order": 11, "cust": 2, "amount": 70}, {"order": 12, "cust": 1, "amount": 20}, {"order": 13, "cust": 9, "amount": 15}]
by_id = {c["id"]: c for c in customers}                                           # build side
inner = [{**o, **{"name": by_id[o["cust"]]["name"]}} for o in orders if o["cust"] in by_id]
left = [{**o, "name": by_id.get(o["cust"], {}).get("name")} for o in orders]       # keep unmatched orders
anti = [o["order"] for o in orders if o["cust"] not in by_id]                      # orders with no customer
print("inner:", [(r["order"], r["name"]) for r in inner])
print("left :", [(r["order"], r["name"]) for r in left])
print("orders without a customer:", anti, "| customers without orders:", [c["name"] for c in customers if c["id"] not in {o["cust"] for o in orders}])
