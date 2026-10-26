def budget_minutes(slo, days=30): return (1 - slo) * days * 24 * 60
for slo in (0.99, 0.995, 0.999, 0.9999, 0.99999):
    print(f"SLO {slo * 100:g}%: error budget {budget_minutes(slo):>8.1f} minutes per 30 days")
