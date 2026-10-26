from decimal import Decimal, ROUND_HALF_UP, getcontext
from fractions import Fraction
print("0.1 + 0.2 =", 0.1 + 0.2, "| equal to 0.3?", 0.1 + 0.2 == 0.3)
print("Decimal:", Decimal("0.1") + Decimal("0.2"), "| equal to 0.3?", Decimal("0.1") + Decimal("0.2") == Decimal("0.3"))
price = Decimal("19.995")
print("round half up:", price.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP), "| built-in round (banker's):", round(2.5), round(3.5))
print("Fraction:", Fraction(1, 3) + Fraction(1, 6), "| from float string:", Fraction("0.75"), "| limit_denominator:", Fraction(3.14159).limit_denominator(100))
getcontext().prec = 30
print("high precision 1/7:", Decimal(1) / Decimal(7))
