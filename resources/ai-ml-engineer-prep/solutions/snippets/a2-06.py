prior, sens, spec = 0.01, 0.95, 0.90
p_pos = sens * prior + (1 - spec) * (1 - prior)
posterior = sens * prior / p_pos
print("P(disease | positive) = %.3f" % posterior)
