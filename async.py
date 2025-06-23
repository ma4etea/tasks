import asyncio


async def get_value(value: str, sec: int):
    print("start", value)
    await asyncio.sleep(sec)
    print("done", value)
    return value


async def main():
    gather_result = await asyncio.gather(
        get_value("gather1", 1),
        get_value("gather2", 2),
    )

    task1 = asyncio.create_task(get_value("task1", 1))
    task2 = asyncio.create_task(get_value("task2", 3))
    await task1
    await task2
    print(gather_result, task1.result(), task2.result())


asyncio.run(main())
