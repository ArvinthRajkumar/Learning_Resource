in_tok, out_tok = 3000, 400
price_in, price_out = 3.0 / 1e6, 15.0 / 1e6           # dollars per token (example prices)
cost = in_tok * price_in + out_tok * price_out
print("cost per request $%.4f; per 1M requests $%.0f" % (cost, cost * 1e6))
cached = in_tok * price_in * 0.1 * 0.8 + in_tok * price_in * 0.2 + out_tok * price_out      # 80% of the prompt cached at 10% price
print("with prompt caching of 80%% of the prompt: $%.4f" % cached)
