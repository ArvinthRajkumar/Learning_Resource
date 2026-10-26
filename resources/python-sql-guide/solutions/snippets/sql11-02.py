import random, bisect
random.seed(3)
n = 100_000
country = random.choices(["IN", "US", "DE", "BR", "XX"], weights=[50, 30, 12, 7, 1], k=n)       # skewed distribution
age = [min(90, max(18, int(random.gauss(40, 12)))) for _ in range(n)]
distinct = len(set(country))
est_naive = n / distinct                                                                         # assumes a uniform distribution
actual_in = country.count("IN"); actual_xx = country.count("XX")
mcv = {c: country.count(c) / n for c in set(country)}                                             # what MCV statistics store
print(f"country = 'IN': naive estimate {est_naive:,.0f} | MCV estimate {mcv['IN'] * n:,.0f} | actual {actual_in:,}")
print(f"country = 'XX': naive estimate {est_naive:,.0f} | MCV estimate {mcv['XX'] * n:,.0f} | actual {actual_xx:,}")
sel_age = sum(1 for a in age if a >= 60) / n
sel_both_indep = mcv["IN"] * sel_age
actual_both = sum(1 for c, a in zip(country, age) if c == "IN" and a >= 60) / n
print(f"IN and age >= 60: independence estimate {sel_both_indep * n:,.0f} vs actual {actual_both * n:,.0f} (columns are independent here, so they agree)")
