import statistics as st, random, math, secrets
data = [2, 4, 4, 4, 5, 5, 7, 9]
print("mean", st.mean(data), "| median", st.median(data), "| mode", st.mode(data), "| pstdev", round(st.pstdev(data), 3), "| stdev", round(st.stdev(data), 3))
print("quantiles:", st.quantiles(data, n=4))
random.seed(42)
print("seeded sample:", random.sample(range(100), 5), "| choice:", random.choice("abcdef"), "| shuffled:", random.sample([1, 2, 3, 4], 4))
print("isclose:", math.isclose(0.1 + 0.2, 0.3), "| gcd:", math.gcd(84, 36), "| comb:", math.comb(10, 3), "| hypot:", math.hypot(3, 4))
token = secrets.token_hex(8)
print("secure token length:", len(token), "(use secrets, not random, for passwords and tokens)")
