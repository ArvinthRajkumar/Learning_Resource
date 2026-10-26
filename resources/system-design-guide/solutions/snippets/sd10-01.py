slo = 0.999
minutes_month = 30 * 24 * 60
budget = (1 - slo) * minutes_month
print("budget:", round(budget, 1), "minutes per 30 days")
used = 18
print("remaining after an 18 minute outage:", round(budget - used, 1))
