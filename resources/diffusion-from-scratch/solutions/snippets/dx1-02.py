import math
T = 1000
betas = [1e-4 + (0.02 - 1e-4) * i / (T - 1) for i in range(T)]
alphas = [1 - b for b in betas]
ab = []
p = 1.0
for a in alphas:
    p *= a
    ab.append(p)

t = 400                      # index of x_t; x_(t-1) uses ab[t-1]
x0, xt = 0.8, 0.3
a_t, b_t, ab_t, ab_prev = alphas[t], betas[t], ab[t], ab[t - 1]

# direct Bayes: prior x_(t-1) | x0 ~ N(sqrt(ab_prev) x0, 1 - ab_prev); likelihood xt | x_(t-1) ~ N(sqrt(a_t) x_(t-1), b_t)
prior_mean, prior_var = math.sqrt(ab_prev) * x0, 1 - ab_prev
precision = 1 / prior_var + a_t / b_t
post_var = 1 / precision
post_mean = post_var * (prior_mean / prior_var + math.sqrt(a_t) * xt / b_t)

# closed form from the formula
mu = (math.sqrt(ab_prev) * b_t / (1 - ab_t)) * x0 + (math.sqrt(a_t) * (1 - ab_prev) / (1 - ab_t)) * xt
var = (1 - ab_prev) / (1 - ab_t) * b_t
print(round(post_mean - mu, 12), round(post_var - var, 12))
print("posterior std is %.5f vs beta std %.5f" % (math.sqrt(var), math.sqrt(b_t)))
