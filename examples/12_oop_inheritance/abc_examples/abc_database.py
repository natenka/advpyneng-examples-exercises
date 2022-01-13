from abc import ABC, abstractmethod
import sqlite3


class BaseDB(ABC):
    def __init__(self, db):
        self.db = db

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def write(self):
        pass

    @abstractmethod
    def read(self):
        pass


class Sqlite(BaseDB):
    def connect(self):
        self.connection = sqlite3.connect(self.db)

    def read(self):
        pass

    def write(self):
        pass
