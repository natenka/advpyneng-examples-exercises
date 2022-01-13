from abc import ABC, abstractmethod


class BaseFilter(ABC):
    @abstractmethod
    def filter(self, value):
        return str(value)


class FilterName(BaseFilter):
    def filter(self, name):
        print(f"FilterName filter {name}")
        print(f"{super().filter(name)=}")
