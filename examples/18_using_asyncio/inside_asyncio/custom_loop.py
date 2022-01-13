import asyncio
from asyncio.events import BaseDefaultEventLoopPolicy as BasePolicy
from rich import inspect
from click import secho


class CustomLoop(type(asyncio.get_event_loop())):
    def _run_once(self):
        # source https://github.com/python/cpython/blob/3.10/Lib/asyncio/base_events.py#L1806
        print(f"RUN ONCE LOOP")
        print(f"    {self._scheduled=}")
        print(f"    {self._ready=}")
        super()._run_once()


class EventLoopPolicy(BasePolicy):
    """Event loop policy.
    The preferred way to make your application use uvloop:
    >>> import asyncio
    >>> import uvloop
    >>> asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    >>> asyncio.get_event_loop()
    <uvloop.Loop running=False closed=False debug=False>
    """

    def _loop_factory(self):
        return CustomLoop()


async def dummy(name):
    secho(f"dummy start {name=}", fg="red")
    await asyncio.sleep(1)
    secho(f"dummy stop  {name=}", fg="red")


if __name__ == "__main__":
    asyncio.set_event_loop_policy(EventLoopPolicy())
    loop = asyncio.get_event_loop()
    # inspect(loop, all=True)
    task1 = loop.run_until_complete(dummy("dummy1"))
    loop.close()
