from abc import ABC, abstractmethod


class BaseFilter(ABC):
    def __init__(self, value):
        self.value = value

    @abstractmethod
    def filter(self):
        pass

    def filter_data(self):
        return self.filter()


class FilterName(BaseFilter):
    def filter(self):
        print(f"FilterName filter")
