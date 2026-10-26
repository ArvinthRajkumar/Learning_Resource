price_in, price_out = 3.00, 15.00                          # dollars per million tokens (illustrative)
def cost(tin, tout, requests): return requests * (tin * price_in + tout * price_out) / 1e6
base = cost(6000, 400, 1_000_000)
trimmed = cost(2500, 400, 1_000_000)
print(f"1M requests/month: ${base:,.0f} with 6000 input tokens vs ${trimmed:,.0f} after trimming context to 2500 ({1 - trimmed / base:.0%} saved)")
