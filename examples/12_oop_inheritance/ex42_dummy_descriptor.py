class Verbose:
    def __get__(self, instance, cls):
        print(f"__get__ {self=} {instance=} {cls=}")

    def __set__(self, instance, value):
        print(f"__set__ {self=} {instance=} {value=}")
