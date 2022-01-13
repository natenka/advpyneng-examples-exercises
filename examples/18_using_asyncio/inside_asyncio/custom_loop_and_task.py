import asyncio
from asyncio.events import BaseDefaultEventLoopPolicy as BasePolicy

from rich import inspect
from click import secho

from custom_task import CustomTask
from custom_loop import EventLoopPolicy


def task_factory(loop, coro):
    return CustomTask(coro, loop=loop)


async def do_nothing():
    await asyncio.sleep(1)


async def dummy(name):
    secho(f"dummy start {name=}", fg="red")
    await do_nothing()
    secho(f"dummy stop  {name=}", fg="red")


if __name__ == "__main__":
    asyncio.set_event_loop_policy(EventLoopPolicy())
    loop = asyncio.get_event_loop()
    loop.set_task_factory(task_factory)
    # inspect(loop, all=True)
    task1 = loop.run_until_complete(dummy("dummy1"))
    loop.close()
