def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    else:
        return "C"
print([grade(s) for s in (95, 85, 40)])
