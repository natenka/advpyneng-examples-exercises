from abc import ABC, abstractmethod
import json


class BaseFile(ABC):
    def __init__(self, filename):
        self.filename = filename

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self, data):
        pass


class TextFile(BaseFile):
    def read(self):
        with open(self.filename) as f:
            return f.read()

    def write(self, data):
        with open(self.filename, "w") as f:
            f.write(data)


class JsonFile(BaseFile):
    def read(self):
        with open(self.filename) as f:
            return json.load(f)

    def write(self, data):
        with open(self.filename, "w") as f:
            json.dump(data, f)
