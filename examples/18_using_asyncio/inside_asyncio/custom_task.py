# source https://github.com/python/cpython/blob/bb76410824e526ee075eac22812a577cca7583cf/Lib/asyncio/tasks.py#L74
import asyncio
from asyncio.tasks import _PyTask
from click import secho


class CustomTask(_PyTask):
    def __init__(self, coro, *, loop=None, name=None):
        super().__init__(coro, loop=loop, name=name)
        self._total_step = 0

    def _Task__step(self, exc=None):
        self._total_step += 1
        secho(f"==> STEP{self._total_step} {self}", fg="green")
        super()._Task__step(exc=exc)
        secho(f"<== STEP{self._total_step} {self}", fg="green")

    def __repr__(self):
        orig_repr = super().__repr__()
        return f"CustomTask {orig_repr}"


async def dummy(name):
    secho(f"dummy start {name=}", fg="red")
    await asyncio.sleep(1)
    await asyncio.sleep(1)
    secho(f"dummy stop  {name=}", fg="red")


async def main():
    print(">>> START")
    await CustomTask(dummy("D1"), name="Task1")
    await CustomTask(dummy("D2"), name="Task2")
    await CustomTask(dummy("D3"), name="Task3")
    print("<<< STOP")


if __name__ == "__main__":
    asyncio.run(main())
