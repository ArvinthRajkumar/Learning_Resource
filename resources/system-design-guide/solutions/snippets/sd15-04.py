# Double-entry: every transfer is a debit and an equal credit; the ledger always balances.
ledger = []
def transfer(src, dst, amount, ref):
    ledger.append((ref, src, -amount))
    ledger.append((ref, dst, +amount))
transfer("customer", "merchant", 100, "pay-1")
transfer("merchant", "customer", 30, "refund-1")
balances = {}
for ref, acct, amt in ledger:
    balances[acct] = balances.get(acct, 0) + amt
print(balances, "sum =", sum(balances.values()))
