import math, random
random.seed(1)
data = [random.gauss(5.0, 2.0) for _ in range(30)]                 # unknown mean and std
def log_post(mu, sigma):
    if sigma <= 0: return -math.inf
    ll = sum(-math.log(sigma) - (x - mu) ** 2 / (2 * sigma ** 2) for x in data)
    log_prior = -mu ** 2 / (2 * 100 ** 2) - sigma / 10               # vague priors
    return ll + log_prior
mu, sigma, lp = 0.0, 1.0, log_post(0.0, 1.0)
samples, accepted = [], 0
for step in range(30000):
    mu2, sigma2 = mu + random.gauss(0, 0.4), sigma + random.gauss(0, 0.3)
    lp2 = log_post(mu2, sigma2)
    if math.log(random.random()) < lp2 - lp: mu, sigma, lp = mu2, sigma2, lp2; accepted += 1
    if step >= 5000: samples.append((mu, sigma))                    # discard burn-in
mus = sorted(s[0] for s in samples); sigmas = sorted(s[1] for s in samples)
q = lambda xs, p: xs[int(p * len(xs))]
print(f"acceptance rate {accepted / 30000:.2f} (about 0.2 to 0.5 is healthy)")
print(f"mean mu: posterior median {q(mus, 0.5):.2f}, 95% interval ({q(mus, 0.025):.2f}, {q(mus, 0.975):.2f}) | sample mean of data {sum(data) / len(data):.2f}")
print(f"std sigma: posterior median {q(sigmas, 0.5):.2f}, 95% interval ({q(sigmas, 0.025):.2f}, {q(sigmas, 0.975):.2f}) | true value 2.0")
