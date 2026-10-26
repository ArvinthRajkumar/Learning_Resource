def flat(total): return total * 0.0
def percent(p): return lambda total: total * p
def tiered(total): return total * (0.2 if total > 100 else 0.05)
def checkout(total, discount): return round(total - discount(total), 2)
print(checkout(200, flat), checkout(200, percent(0.1)), checkout(200, tiered), checkout(50, tiered))
