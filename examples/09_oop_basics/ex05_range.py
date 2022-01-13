
class MyRange:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self._last = start

    def __next__(self):
        print("__next__")
        value = self._last
        if value == self.stop:
            raise StopIteration
        self._last += 1
        return value
