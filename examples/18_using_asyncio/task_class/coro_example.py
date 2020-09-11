import asyncio
from task_class_simple import Task, _all_tasks


tasks = []


async def coro1():
    print("coro1 Start")
    await asyncio.sleep(3)
    print("coro1 Working")
    await asyncio.sleep(1)
    print("coro1 End")


async def coro2():
    print("coro2 Start")
    await Task(coro1(), name="coro1")
    print("coro2 End")


async def main():
    task2 = Task(coro2(), name="coro2")
    tasks.append(task2)
    await asyncio.gather(task2)
    del task2


asyncio.run(main())

"""
Task coro2 __init__
Task coro2 _step
coro2 Start
Task coro1 __init__
Task coro1 _step
coro1 Start
Task coro1 _wakeup
Task coro1 _step
coro1 Working
Task coro1 _wakeup
Task coro1 _step
coro1 End
Task coro2 _wakeup
Task coro2 _step
coro2 End
"""
