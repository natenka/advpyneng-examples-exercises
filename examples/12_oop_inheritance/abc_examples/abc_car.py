from abc import ABC, abstractmethod


class BaseCar(ABC):
    def drive_forward(self):
        pass

    def stop(self):
        pass

    def drive_backward(self):
        pass

    def turn_left(self):
        pass

    def turn_right(self):
        pass
