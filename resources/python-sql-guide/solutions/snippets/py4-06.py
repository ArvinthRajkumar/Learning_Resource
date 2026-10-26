import asyncio

async def slow():
    await asyncio.sleep(5)
    return "never"

async def main():
    task = asyncio.create_task(asyncio.sleep(0.05, result="background"))
    print("main continues")
    print(await task)
    try:
        await asyncio.wait_for(slow(), timeout=0.1)
    except asyncio.TimeoutError:
        print("timed out and cancelled")
    async with asyncio.timeout(1):
        print("inside timeout block")

asyncio.run(main())
