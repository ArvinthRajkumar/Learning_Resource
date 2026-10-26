processed = set()
balance = {"acct": 100}

def handle(msg):
    if msg["id"] in processed:          # deduplicate
        return "duplicate ignored"
    balance["acct"] += msg["amount"]
    processed.add(msg["id"])
    return "applied"

m = {"id": "pay-123", "amount": 25}
print(handle(m), handle(m), handle(m), balance)   # redelivered three times
