import inspect


class SourceCodeMixin:
    def source(self):
        return inspect.getsource(self.__class__)


class AttributesMixin:
    @property
    def attributes(self):
        # data attributes
        for name, value in self.__dict__.items():
            print(f"{name:25}{str(value):<20}")
        # methods
        for name, value in self.__class__.__dict__.items():
            if not name.startswith('__'):
                print(f"{name:25}{str(value):<20}")

