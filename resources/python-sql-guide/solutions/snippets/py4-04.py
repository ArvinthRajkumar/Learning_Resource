from concurrent.futures import ProcessPoolExecutor

def is_prime(n):
    if n < 2: return False
    i = 2
    while i * i <= n:
        if n % i == 0: return False
        i += 1
    return True

if __name__ == "__main__":          # required on Windows and macOS (spawn start method)
    nums = [1_000_003, 1_000_033, 1_000_037, 1_000_039]
    with ProcessPoolExecutor(max_workers=2) as pool:
        print(list(pool.map(is_prime, nums)))
