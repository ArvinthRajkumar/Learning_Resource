import subprocess, sys
r = subprocess.run([sys.executable, "-c", "print('child says hi'); import sys; sys.exit(3)"], capture_output=True, text=True)
print("stdout:", r.stdout.strip(), "| return code:", r.returncode)
try:
    subprocess.run([sys.executable, "-c", "raise SystemExit(1)"], check=True)
except subprocess.CalledProcessError as e:
    print("check=True raised: exit status", e.returncode)
try:
    subprocess.run([sys.executable, "-c", "import time; time.sleep(5)"], timeout=0.3)
except subprocess.TimeoutExpired:
    print("timeout enforced")
