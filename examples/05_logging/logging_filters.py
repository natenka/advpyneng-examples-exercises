import logging


class MessageFilter(logging.Filter):
    def __init__(self, contains):
        self.contains = contains

    def filter(self, record):
        return self.contains in record.msg


class DebugOnlyFilter(logging.Filter):
    def filter(self, record):
        return record.levelno == logging.DEBUG


class LevelFilter(logging.Filter):
    def __init__(self, level):
        self.level = level

    def filter(self, record):
        return record.levelno == self.level


class LevelAndMessageFilter(logging.Filter):
    def __init__(self, level, message):
        self.level = LevelFilter(level)
        self.message = MessageFilter(message)

    def filter(self, record):
        return self.level.filter(record) and self.message.filter(record)

