import inspect


class SourceCodeMixin:
    def source(self):
        return inspect.getsource(self.__class__)
