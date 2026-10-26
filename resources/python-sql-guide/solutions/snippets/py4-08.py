import asyncio

async def job(n):
    await asyncio.sleep(0.01)
    return n * 10

async def main():
    async with asyncio.TaskGroup() as tg:
        tasks = [tg.create_task(job(i)) for i in range(3)]
    print([t.result() for t in tasks])

asyncio.run(main())
