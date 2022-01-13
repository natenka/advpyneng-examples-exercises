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
