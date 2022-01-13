class Task(futures._PyFuture):  # Inherit Python Task implementation
    # from a Python Future implementation.

    """A coroutine wrapped in a Future."""

    # An important invariant maintained while a Task not done:
    #
    # - Either _fut_waiter is None, and _step() is scheduled;
    # - or _fut_waiter is some Future, and _step() is *not* scheduled.
    #
    # The only transition from the latter to the former is through
    # _wakeup().  When _fut_waiter is not None, one of its callbacks
    # must be _wakeup().

    # If False, don't log a message if the task is destroyed whereas its
    # status is still pending
    _log_destroy_pending = True

    def __init__(self, coro, *, loop=None, name=None):
        super().__init__(loop=loop)
        if self._source_traceback:
            del self._source_traceback[-1]
        if not coroutines.iscoroutine(coro):
            # raise after Future.__init__(), attrs are required for __del__
            # prevent logging for pending task in __del__
            self._log_destroy_pending = False
            raise TypeError(f"a coroutine was expected, got {coro!r}")

        if name is None:
            self._name = f"Task-{_task_name_counter()}"
        else:
            self._name = str(name)

        self._must_cancel = False
        self._fut_waiter = None
        self._coro = coro
        self._context = contextvars.copy_context()

        self._loop.call_soon(self.__step, context=self._context)
        _register_task(self)

    def __del__(self):
        if self._state == futures._PENDING and self._log_destroy_pending:
            context = {
                "task": self,
                "message": "Task was destroyed but it is pending!",
            }
            if self._source_traceback:
                context["source_traceback"] = self._source_traceback
            self._loop.call_exception_handler(context)
        super().__del__()

    def __class_getitem__(cls, type):
        return cls

    def _repr_info(self):
        return base_tasks._task_repr_info(self)

    def get_coro(self):
        return self._coro

    def get_name(self):
        return self._name

    def set_name(self, value):
        self._name = str(value)

    def set_result(self, result):
        raise RuntimeError("Task does not support set_result operation")

    def set_exception(self, exception):
        raise RuntimeError("Task does not support set_exception operation")

    def get_stack(self, *, limit=None):
        """Return the list of stack frames for this task's coroutine.
        If the coroutine is not done, this returns the stack where it is
        suspended.  If the coroutine has completed successfully or was
        cancelled, this returns an empty list.  If the coroutine was
        terminated by an exception, this returns the list of traceback
        frames.
        The frames are always ordered from oldest to newest.
        The optional limit gives the maximum number of frames to
        return; by default all available frames are returned.  Its
        meaning differs depending on whether a stack or a traceback is
        returned: the newest frames of a stack are returned, but the
        oldest frames of a traceback are returned.  (This matches the
        behavior of the traceback module.)
        For reasons beyond our control, only one stack frame is
        returned for a suspended coroutine.
        """
        return base_tasks._task_get_stack(self, limit)

    def print_stack(self, *, limit=None, file=None):
        """Print the stack or traceback for this task's coroutine.
        This produces output similar to that of the traceback module,
        for the frames retrieved by get_stack().  The limit argument
        is passed to get_stack().  The file argument is an I/O stream
        to which the output is written; by default output is written
        to sys.stderr.
        """
        return base_tasks._task_print_stack(self, limit, file)

    def cancel(self, msg=None):
        """Request that this task cancel itself.
        This arranges for a CancelledError to be thrown into the
        wrapped coroutine on the next cycle through the event loop.
        The coroutine then has a chance to clean up or even deny
        the request using try/except/finally.
        Unlike Future.cancel, this does not guarantee that the
        task will be cancelled: the exception might be caught and
        acted upon, delaying cancellation of the task or preventing
        cancellation completely.  The task may also return a value or
        raise a different exception.
        Immediately after this method is called, Task.cancelled() will
        not return True (unless the task was already cancelled).  A
        task will be marked as cancelled when the wrapped coroutine
        terminates with a CancelledError exception (even if cancel()
        was not called).
        """
        self._log_traceback = False
        if self.done():
            return False
        if self._fut_waiter is not None:
            if self._fut_waiter.cancel(msg=msg):
                # Leave self._fut_waiter; it may be a Task that
                # catches and ignores the cancellation so we may have
                # to cancel it again later.
                return True
        # It must be the case that self.__step is already scheduled.
        self._must_cancel = True
        self._cancel_message = msg
        return True

    def __step(self, exc=None):
        if self.done():
            raise exceptions.InvalidStateError(
                f"_step(): already done: {self!r}, {exc!r}"
            )
        if self._must_cancel:
            if not isinstance(exc, exceptions.CancelledError):
                exc = self._make_cancelled_error()
            self._must_cancel = False
        coro = self._coro
        self._fut_waiter = None

        _enter_task(self._loop, self)
        # Call either coro.throw(exc) or coro.send(None).
        try:
            if exc is None:
                # We use the `send` method directly, because coroutines
                # don't have `__iter__` and `__next__` methods.
                result = coro.send(None)
            else:
                result = coro.throw(exc)
        except StopIteration as exc:
            if self._must_cancel:
                # Task is cancelled right before coro stops.
                self._must_cancel = False
                super().cancel(msg=self._cancel_message)
            else:
                super().set_result(exc.value)
        except exceptions.CancelledError as exc:
            # Save the original exception so we can chain it later.
            self._cancelled_exc = exc
            super().cancel()  # I.e., Future.cancel(self).
        except (KeyboardInterrupt, SystemExit) as exc:
            super().set_exception(exc)
            raise
        except BaseException as exc:
            super().set_exception(exc)
        else:
            blocking = getattr(result, "_asyncio_future_blocking", None)
            if blocking is not None:
                # Yielded Future must come from Future.__iter__().
                if futures._get_loop(result) is not self._loop:
                    new_exc = RuntimeError(
                        f"Task {self!r} got Future "
                        f"{result!r} attached to a different loop"
                    )
                    self._loop.call_soon(self.__step, new_exc, context=self._context)
                elif blocking:
                    if result is self:
                        new_exc = RuntimeError(f"Task cannot await on itself: {self!r}")
                        self._loop.call_soon(
                            self.__step, new_exc, context=self._context
                        )
                    else:
                        result._asyncio_future_blocking = False
                        result.add_done_callback(self.__wakeup, context=self._context)
                        self._fut_waiter = result
                        if self._must_cancel:
                            if self._fut_waiter.cancel(msg=self._cancel_message):
                                self._must_cancel = False
                else:
                    new_exc = RuntimeError(
                        f"yield was used instead of yield from "
                        f"in task {self!r} with {result!r}"
                    )
                    self._loop.call_soon(self.__step, new_exc, context=self._context)

            elif result is None:
                # Bare yield relinquishes control for one event loop iteration.
                self._loop.call_soon(self.__step, context=self._context)
            elif inspect.isgenerator(result):
                # Yielding a generator is just wrong.
                new_exc = RuntimeError(
                    f"yield was used instead of yield from for "
                    f"generator in task {self!r} with {result!r}"
                )
                self._loop.call_soon(self.__step, new_exc, context=self._context)
            else:
                # Yielding something else is an error.
                new_exc = RuntimeError(f"Task got bad yield: {result!r}")
                self._loop.call_soon(self.__step, new_exc, context=self._context)
        finally:
            _leave_task(self._loop, self)
            self = None  # Needed to break cycles when an exception occurs.

    def __wakeup(self, future):
        try:
            future.result()
        except BaseException as exc:
            # This may also be a cancellation.
            self.__step(exc)
        else:
            # Don't pass the value of `future.result()` explicitly,
            # as `Future.__iter__` and `Future.__await__` don't need it.
            # If we call `_step(value, None)` instead of `_step()`,
            # Python eval loop would use `.send(value)` method call,
            # instead of `__next__()`, which is slower for futures
            # that return non-generator iterators from their `__iter__`.
            self.__step()
        self = None  # Needed to break cycles when an exception occurs.
