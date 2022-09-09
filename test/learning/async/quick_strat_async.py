import asyncio
from time import sleep


async def func():
    print("测试ing")
    response = await other()
    print("结束",response)
result=func()

async def other():
    await asyncio.sleep(2)
    return "返回值"


# await + 可等待的对象(协程对象 \ Futrue \Task对象   ->IO等待)

if __name__ == "__main__":
    # loop=asyncio.get_event_loop()
    # loop.run_until_complete(result)

    # python3.7 以后可用
    asyncio.run(result)
