def burn_rate(error_rate, slo): return error_rate / (1 - slo)
def hours_to_exhaust(rate, days=30): return days * 24 / rate
slo = 0.999
for err in (0.0005, 0.001, 0.0144, 0.05):
    r = burn_rate(err, slo)
    print(f"error rate {err:.2%}: burn rate {r:>6.1f} -> budget exhausted in {hours_to_exhaust(r) / 24:>7.2f} days")
