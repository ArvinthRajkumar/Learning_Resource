import threading

counter = 0
lock = threading.Lock()

def work(n):
    global counter
    for _ in range(n):
        with lock:                # only one thread at a time in this block
            counter += 1

threads = [threading.Thread(target=work, args=(10000,)) for _ in range(4)]
for t in threads: t.start()
for t in threads: t.join()
print(counter)
