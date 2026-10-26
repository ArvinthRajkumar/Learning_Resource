import asyncio

async def main():
    sem = asyncio.Semaphore(3)
    running, peak = 0, 0
    async def task(i):
        nonlocal running, peak
        async with sem:
            running += 1
            peak = max(peak, running)
            await asyncio.sleep(0.01)
            running -= 1
        return i * i
    results = await asyncio.gather(*(task(i) for i in range(10)))
    print(results, "peak concurrency:", peak)
asyncio.run(main())
