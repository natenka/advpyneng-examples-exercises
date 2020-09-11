from collections import deque
import asyncio
from task_class_simple import Task


class Scheduler:
    def __init__(self):
        self.tasks = deque()
        self.done = {}
        self.failed = {}

    def add_task(self, task):
        self.tasks.append(task)

    def run(self):
        while len(self.tasks) != 0:
            task = self.tasks.popleft()
            print("Running task...")
            try:
                task._step()
            except StopIteration as e:
                print("Task completed")
                self.done[task.name] = e.value
            except Exception as e:
                self.failed[task.name] = e
            else:
                self.tasks.append(task)


async def coro1():
    print("Start")
    await asyncio.sleep(3)
    print("Working")
    await asyncio.sleep(1)
    print("End")


async def coro2():
    print("Start")
    await Task(asyncio.sleep(3), name="sleep coro2")
    print("End")


async def main():
    task1 = Task(coro1(), name="coro1")
    task2 = Task(coro2(), name="coro2")

    s = Scheduler()
    s.add_task(task1)
    s.add_task(task2)
    s.run()
    # await asyncio.gather(task1, task2)


asyncio.run(main())
