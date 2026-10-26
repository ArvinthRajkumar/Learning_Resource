def run_saga(steps, fail_at=None):
    done, log = [], []
    for i, (name, action, compensate) in enumerate(steps):
        if i == fail_at:
            log.append(f"{name}: FAILED")
            for n, c in reversed(done):
                log.append(f"compensate {n}: {c()}")
            return False, log
        log.append(f"{name}: {action()}")
        done.append((name, compensate))
    return True, log
steps = [
    ("reserve stock", lambda: "reserved", lambda: "released"),
    ("charge card", lambda: "charged", lambda: "refunded"),
    ("create shipment", lambda: "created", lambda: "cancelled"),
]
for fail_at in (None, 2):
    ok, log = run_saga(steps, fail_at)
    print("success" if ok else "rolled back", "->", " | ".join(log))
