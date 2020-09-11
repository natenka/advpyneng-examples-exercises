# source https://www.pythonsheets.com/appendix/python-asyncio.html
import weakref
import asyncio

Future = asyncio.futures.Future

# WeakSet containing all alive tasks.
_all_tasks = weakref.WeakSet()


def _register_task(task):
    """Register a new task in asyncio as executed by loop."""
    _all_tasks.add(task)


class Task(Future):
    """Simple prototype of Task"""

    def __init__(self, coro, *, loop=None, name=None):
        self.name = name
        print(f"Task {self.name} __init__")
        super().__init__(loop=loop)
        self._coro = coro
        self._loop.call_soon(self._step)
        _register_task(self)

    def _step(self, val=None, exc=None):
        print(f"Task {self.name} _step")
        try:
            if exc:
                f = self._coro.throw(exc)
            else:
                f = self._coro.send(val)
        except StopIteration as e:
            self.set_result(e.value)
        except Exception as e:
            self.set_exception(e)
        else:
            f.add_done_callback(self._wakeup)

    def _wakeup(self, fut):
        print(f"Task {self.name} _wakeup")
        try:
            res = fut.result()
        except Exception as e:
            self._step(None, e)
        else:
            self._step(res, None)

    def __repr__(self):
        return f"Task({self.name})"
