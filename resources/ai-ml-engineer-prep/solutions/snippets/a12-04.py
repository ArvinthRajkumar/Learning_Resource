# A minimal agent loop with a scripted "model" so the control flow is visible and deterministic.
def fake_model(history):
    if not any(h.startswith("TOOL_RESULT") for h in history):
        return {"tool": "calculator", "args": "17 * 23"}
    return {"final": "17 x 23 = " + [h for h in history if h.startswith("TOOL_RESULT")][-1].split(":")[1]}
def calculator(expr):
    a, op, b = expr.split()
    return str({"*": int(a) * int(b), "+": int(a) + int(b)}[op])
history, steps = ["USER: what is 17 * 23?"], 0
while steps < 5:                                             # always cap the loop
    out = fake_model(history); steps += 1
    if "final" in out:
        print(out["final"]); break
    history.append("TOOL_RESULT:" + calculator(out["args"]))
print("steps used:", steps)
