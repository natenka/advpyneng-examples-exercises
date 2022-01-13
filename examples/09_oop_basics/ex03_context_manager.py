import time


class Timed:
    def __enter__(self):
        print("__enter__")
        self.start = time.time()
        return 42

    def __exit__(self, exc_type, exc_value, traceback):
        print(exc_type, exc_value, traceback)
        print("__exit__")
        end = time.time()
        print("время выполнения", end - self.start)
