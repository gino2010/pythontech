# synchronous
# author gino
# created on 2018/4/21
import asyncio
import time
from datetime import datetime


# 虽然方法异步，但是sleep同步，使得整个异步调用都同步了
# method is async, but sleep is sync, so make all async tasks synchronized
async def sync_sleep():
    print('sleep', datetime.now())
    time.sleep(1)


# 应该是使用asyncio中的sleep
# should use sleep method in asyncio
async def async_sleep():
    print('sleep', datetime.now())
    await asyncio.sleep(1)


async def factorial(name, number, sync=True):
    _result = 1

    for i in range(2, number + 1):
        print('Task {}: Compute factorial({})'.format(name, i))
        if sync:
            await sync_sleep()
        else:
            await async_sleep()
        _result *= i

    print('Task {}: factorial({}) is {}\n'.format(name, number, _result))


if __name__ == '__main__':
    start = time.time()
    loop = asyncio.get_event_loop()

    task = [
        asyncio.ensure_future(factorial("A", 3)),
        asyncio.ensure_future(factorial("B", 4)),
    ]

    loop.run_until_complete(asyncio.wait(task))

    print('----------------------------------')

    task = [
        asyncio.ensure_future(factorial("A", 3, False)),
        asyncio.ensure_future(factorial("B", 4, False)),
    ]

    loop.run_until_complete(asyncio.wait(task))

    loop.close()

    end = time.time()
    print("Total time: {}".format(end - start))
