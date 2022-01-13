from task_custom import Task
import asyncio


async def coro(name):
    print(f">> Start {name}")
    await asyncio.sleep(1)
    print(f">> Working.. {name}")
    await asyncio.sleep(1)
    print(f">> End {name}")


async def main():
    task1 = Task(coro("coro1"), name="task1")
    task2 = Task(coro("coro2"), name="task2")
    await task1
    await task2
    #print(task1, task2)


asyncio.run(main())

'''
Task task1 __init__
Task task1 _step
>> Start coro1
Task task1 _wakeup
Task task1 _step
>> Working.. coro1
Task task1 _wakeup
Task task1 _step
>> End coro1

'''
