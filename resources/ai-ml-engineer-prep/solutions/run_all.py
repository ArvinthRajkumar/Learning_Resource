"""Run every test file under solutions/ and print a summary.

Usage (from anywhere):  python3 resources/ai-ml-engineer-prep/solutions/run_all.py
Each test runs in its own process with its folder as the working directory,
so the files can import their neighbours with plain imports.
"""
import pathlib
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent


def main() -> int:
    files = sorted(HERE.rglob("test_*.py")) + sorted(HERE.glob("verify_*.py"))
    failed = 0
    t0 = time.perf_counter()
    for f in files:
        start = time.perf_counter()
        r = subprocess.run([sys.executable, f.name], cwd=f.parent, capture_output=True, text=True)
        dt = time.perf_counter() - start
        rel = f.relative_to(HERE)
        if r.returncode == 0:
            last = (r.stdout.strip().splitlines() or ["ok"])[-1]
            print(f"PASS  {rel}  ({dt:.1f}s)  {last}")
        else:
            failed += 1
            print(f"FAIL  {rel}  ({dt:.1f}s)")
            print(r.stdout[-2000:])
            print(r.stderr[-4000:])
    print(f"\n{len(files) - failed}/{len(files)} test files passed in {time.perf_counter() - t0:.1f}s")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
