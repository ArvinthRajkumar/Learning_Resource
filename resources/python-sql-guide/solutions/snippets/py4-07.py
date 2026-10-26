import asyncio

async def worker(name, q, out, sem):
    while True:
        item = await q.get()
        async with sem:                   # limit concurrency
            await asyncio.sleep(0.01)
            out.append((name, item))
        q.task_done()

async def main():
    q, out, sem = asyncio.Queue(), [], asyncio.Semaphore(2)
    workers = [asyncio.create_task(worker(f"w{i}", q, out, sem)) for i in range(3)]
    for i in range(6): q.put_nowait(i)
    await q.join()                        # wait until all items are processed
    for w in workers: w.cancel()
    print(sorted(item for _, item in out))

asyncio.run(main())
