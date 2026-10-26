users, actions_per_user, bytes_each = 100_000_000, 5, 2_000
per_second = users * actions_per_user / 86_400
print(f"average {per_second:,.0f} requests/s, peak (x3) about {per_second * 3:,.0f}/s")
print(f"storage per year: {users * actions_per_user * bytes_each * 365 / 1e12:,.0f} TB | bandwidth at peak: {per_second * 3 * bytes_each * 8 / 1e9:.1f} Gbit/s")
