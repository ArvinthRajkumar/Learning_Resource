checklist = {
    "Intended use and out-of-scope uses written down": True,
    "Training data provenance and consent documented": True,
    "Metrics reported per slice (not only overall)": False,
    "Fairness criteria chosen with stakeholders": False,
    "Privacy review and retention policy": True,
    "Adversarial and misuse testing done": False,
    "Human oversight and appeal path defined": True,
    "Monitoring and rollback plan in place": True,
}
missing = [k for k, v in checklist.items() if not v]
print(f"{len(checklist) - len(missing)} of {len(checklist)} launch checks done; blocking items:")
for m in missing: print("  -", m)
