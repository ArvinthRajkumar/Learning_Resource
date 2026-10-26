import asyncio

async def fetch(name, delay):
    await asyncio.sleep(delay)            # non-blocking wait
    return f"{name} done"

async def main():
    results = await asyncio.gather(fetch("a", 0.3), fetch("b", 0.2), fetch("c", 0.1))
    print(results)                         # results keep the input order

asyncio.run(main())
