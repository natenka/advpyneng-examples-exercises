import asyncio
import time


async def print_number(task_name):
    print(f">>> Start {task_name}")
    for _ in range(10):
        print(42)
        time.sleep(0.5)
    print(f"<<< End   {task_name}")


async def print_text(task_name):
    print(f">>> Start {task_name}")
    for _ in range(10):
        print("hello")
        await asyncio.sleep(0.9)
    print(f"<<< End   {task_name}")


async def main():
    task1 = asyncio.create_task(print_number("task1"))
    task2 = asyncio.create_task(print_text("task2"))
    await task1
    await task2
