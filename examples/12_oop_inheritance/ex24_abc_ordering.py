from abc import ABC, abstractmethod


class Ordering(ABC):
    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass

    def __ne__(self, other):
        return not self == other

