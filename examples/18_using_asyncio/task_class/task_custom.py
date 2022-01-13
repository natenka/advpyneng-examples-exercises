import asyncio


class Task(asyncio.futures.Future):
    def __init__(self, coro, *, loop=None, name=None):
        self.name = name
        print(f"Task {self.name} __init__")
        super().__init__(loop=loop)
        self.coro = coro
        self._loop.call_soon(self._step)

    def _step(self, val=None, exc=None):
        print(f"Task {self.name} _step")
        try:
            if exc is None:
                # We use the `send` method directly, because coroutines
                # don't have `__iter__` and `__next__` methods.
                future = self.coro.send(None)
            else:
                future = self.coro.throw(exc) #coroutine coro
        except StopIteration as error:
            self.set_result(error.value)
        except Exception as error:
            self.set_exception(error)
        else:
            future.add_done_callback(self._wakeup)

    def _wakeup(self, fut):
        print(f"Task {self.name} _wakeup")
        try:
            res = fut.result()
        except Exception as e:
            self._step(None, e)
        else:
            self._step(res, None)

    def __repr__(self):
        return f"Custom Task {self.name}"
