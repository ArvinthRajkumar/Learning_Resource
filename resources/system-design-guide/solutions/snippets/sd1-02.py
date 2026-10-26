tweets_per_day = 500_000_000
bytes_each = 300
per_day_gb = tweets_per_day * bytes_each / 1e9
per_year_tb = per_day_gb * 365 / 1e3
five_years_tb = per_year_tb * 5
print(per_day_gb, "GB/day")
print(round(per_year_tb, 1), "TB/year")
print(round(five_years_tb), "TB for 5 years")
print(round(five_years_tb * 3), "TB with 3 replicas")
