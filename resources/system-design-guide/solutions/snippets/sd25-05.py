import subprocess, sys, tempfile, os
def judge(code, stdin, expected, timeout=2):
    with tempfile.TemporaryDirectory() as d:
        path = os.path.join(d, "sol.py")
        open(path, "w").write(code)
        try:
            r = subprocess.run([sys.executable, "-I", path], input=stdin, capture_output=True, text=True, timeout=timeout)
        except subprocess.TimeoutExpired:
            return "Time Limit Exceeded"
        if r.returncode != 0: return "Runtime Error"
        return "Accepted" if r.stdout.split() == expected.split() else "Wrong Answer"
good = "a, b = map(int, input().split())" + chr(10) + "print(a + b)"
print(judge(good, "3 4", "7"))
print(judge("print(1)", "", "2"))
print(judge("while True: pass", "", "", timeout=1))
print(judge("raise SystemExit(3)", "", ""))
