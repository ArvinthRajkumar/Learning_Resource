for a in (0.99, 0.999, 0.9995, 0.9999, 0.99999):
    down_min = (1 - a) * 365 * 24 * 60
    print("%.3f%% -> %.1f minutes/year" % (a * 100, down_min))
