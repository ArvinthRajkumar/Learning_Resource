import math, random
random.seed(4)
data = [random.gauss(0, 1) for _ in range(300)] + [random.gauss(5, 1.2) for _ in range(200)]
def normal_pdf(x, mu, s): return math.exp(-0.5 * ((x - mu) / s) ** 2) / (s * math.sqrt(2 * math.pi))
pi, mu, sd = [0.5, 0.5], [-1.0, 1.0], [1.0, 1.0]                 # rough initial guesses
for it in range(60):
    resp = []
    for x in data:                                               # E-step: responsibilities
        p = [pi[k] * normal_pdf(x, mu[k], sd[k]) for k in range(2)]; s = sum(p); resp.append([v / s for v in p])
    for k in range(2):                                           # M-step: weighted re-estimation
        nk = sum(r[k] for r in resp)
        pi[k] = nk / len(data); mu[k] = sum(r[k] * x for r, x in zip(resp, data)) / nk
        sd[k] = math.sqrt(sum(r[k] * (x - mu[k]) ** 2 for r, x in zip(resp, data)) / nk)
ll = sum(math.log(sum(pi[k] * normal_pdf(x, mu[k], sd[k]) for k in range(2))) for x in data)
print("estimated weights:", [round(v, 2) for v in pi], "(true 0.60, 0.40) | means:", [round(v, 2) for v in mu], "(true 0, 5) | stds:", [round(v, 2) for v in sd], "(true 1, 1.2)")
print("log-likelihood:", round(ll, 1))
