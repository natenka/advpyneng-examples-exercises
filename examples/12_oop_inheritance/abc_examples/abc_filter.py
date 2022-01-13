import abc

class BaseFilter(abc.ABC):

    @abc.abstractmethod
    def filter(self):
        pass

    def filter_data(self):
        self.filter()


class FilterByName(BaseFilter):
    def filter(self):
        print("вызываю filter в FilterByName")
        super().filter()






















class BaseFilter2:
    def filter_data(self):
        if hasattr(self, "filter"):
            self.filter()
        else:
            raise AttributeError("Обязательно должен быть метод filter")

class BaseFilter3:
    def filter(self):
        raise NotImplementedError

    def filter_data(self):
        try:
            self.filter()
        except NotImplementedError:
            raise AttributeError("Обязательно должен быть метод filter")
