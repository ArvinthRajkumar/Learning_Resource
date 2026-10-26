import math, random
random.seed(1)
period, n = 7, 70
series = [50 + 0.5 * t + 10 * math.sin(2 * math.pi * (t % period) / period) + random.gauss(0, 1.5) for t in range(n)]    # trend + weekly season + noise
def moving_average(x, w):                                              # centred moving average for odd w
    h = w // 2
    return [sum(x[i - h:i + h + 1]) / w if h <= i < len(x) - h else None for i in range(len(x))]
trend = moving_average(series, period)
detrended = [s - t if t is not None else None for s, t in zip(series, trend)]
seasonal = [sum(d for i, d in enumerate(detrended) if d is not None and i % period == k) / sum(1 for i, d in enumerate(detrended) if d is not None and i % period == k) for k in range(period)]
mean_seasonal = sum(seasonal) / period
seasonal = [s - mean_seasonal for s in seasonal]                       # centre the seasonal profile at zero
true_profile = [10 * math.sin(2 * math.pi * k / period) for k in range(period)]
print("estimated seasonal profile:", [round(s, 1) for s in seasonal])
print("true seasonal profile     :", [round(s, 1) for s in true_profile])
rem = [d - seasonal[i % period] for i, d in enumerate(detrended) if d is not None]
print("remainder std (should be about the noise level 1.5):", round((sum(r * r for r in rem) / len(rem)) ** 0.5, 2))
