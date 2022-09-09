
import asyncio
from contextlib import AsyncExitStack


async def func():
    print(1)
    await asyncio.sleep(2)
    print(2)
    return "返回值"

async def main():
    print("main开始")
    # task1= asyncio.create_task(func())
    # task2 = asyncio.create_task(func())
    task_list=[
        asyncio.create_task(func(),name="n1"),
        asyncio.create_task(func(),name="n2")
    ]
    print("main 结束")

    # res1=await task1
    # res2=await task2
    done,pending=await asyncio.wait(task_list,timeout=2)
    print(done)
    print(pending)

asyncio.run(main())
