import queue, threading

q, results = queue.Queue(), []

def consumer():
    while True:
        item = q.get()
        if item is None:           # sentinel: stop
            break
        results.append(item * 2)
        q.task_done()

t = threading.Thread(target=consumer)
t.start()
for i in range(5):
    q.put(i)
q.put(None)
t.join()
print(results)
