def run_saga(steps, fail_at=None):
    done = []
    for i, (name, do, undo) in enumerate(steps):
        if i == fail_at:
            print("FAIL at", name)
            for dn, dundo in reversed(done):
                print("  compensate", dn); dundo()
            return False
        do(); done.append((name, undo)); print("ok", name)
    return True

noop = lambda: None
steps = [("create order", noop, noop), ("reserve stock", noop, noop), ("charge card", noop, noop)]
run_saga(steps)
print("---")
run_saga(steps, fail_at=2)
