HOURS = 730
compute = 10 * 0.17 * HOURS             # 10 instances at $0.17/h
storage = 5000 * 0.023                  # 5 TB object storage at $0.023/GB-month
egress = 20000 * 0.09                   # 20 TB out at $0.09/GB
db = 2 * 0.60 * HOURS                   # 2 DB nodes at $0.60/h
total = compute + storage + egress + db
for name, v in [("compute", compute), ("object storage", storage), ("data egress", egress), ("database", db)]:
    print(f"{name:>15}: ${v:>9,.0f} ({v / total:5.1%})")
print(f"{'total/month':>15}: ${total:>9,.0f}")
