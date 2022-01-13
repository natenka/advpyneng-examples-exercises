class Cycle:
    def __init__(self, values):
        print("__init__")
        self.values = values # [1, 2, 3]
        self._index = 0

    def __next__(self):
        print("__next__", self._index)
        idx = self._index % len(self.values)
        result = self.values[idx]
        self._index += 1
        return result

    def __iter__(self):
        print("__iter__")
        return self


class Repeat:
    def __init__(self, value):
        print("__init__")
        self.value = value

    def __next__(self):
        print("__next__")
        return self.value

    def __iter__(self):
        print("__iter__")
        return self


class FiniteCycle:
    def __init__(self, values):
        print("__init__")
        self.values = values # [1, 2, 3]
        self._index = 0

    def __next__(self):
        print("__next__")
        try:
            result = self.values[self._index]
            self._index += 1
            return result
        except IndexError:
            raise StopIteration

    def __iter__(self):
        print("__iter__")
        return self
