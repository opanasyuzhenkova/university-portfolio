import asyncio


async def do_task1():
    await asyncio.sleep(2)
    return "task 1 result"


async def do_task2():
    await asyncio.sleep(1)
    return "task 2 result"


def process_results(results):
    for result in results:
        print(f"Result: {result}")


async def main():
    results = await asyncio.gather(do_task1(), do_task2())
    process_results(results)


if __name__ == "__main__":
    asyncio.run(main())
