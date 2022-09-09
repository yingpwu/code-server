import asyncio


async def func1():
    print(1.1)
    await asyncio.sleep(2)
    print(1.2)


async def func2():
    print(2.1)
    await asyncio.sleep(2)
    print(2.2)


tasks = [
    asyncio.ensure_future(func1()),
    asyncio.ensure_future(func2())
]

# 去生成或获取一个时间循环
loop = asyncio.get_event_loop()

# 将任务放到 任务列表
loop.run_until_complete(asyncio.wait(tasks))
