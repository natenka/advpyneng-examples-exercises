import sys
import re
import logging
from rich import inspect

class FilterLevel(logging.Filter):
    def __init__(self, level):
        self.level = level

    def filter(self, record):
        if record.levelname == self.level:
            return True
        else:
            return False


class MessageFilter(logging.Filter):
    def __init__(self, contains):
        self.contains = contains

    def filter(self, record):
        return self.contains in record.msg


class AddIPFilter(logging.Filter):
    def filter(self, record):
        match = re.search(r"\d+\.\d+\.\d+\.\d+", record.msg)
        if match:
            record.ip = match.group()
        else:
            record.ip = None
        return True


fmt = logging.Formatter(
    "{name} {levelname} {ip} {message}",
    style="{"
)
stderr = logging.StreamHandler()
stderr.setLevel(logging.DEBUG)
stderr.setFormatter(fmt)
# stderr.addFilter(FilterLevel("DEBUG"))
# stderr.addFilter(MessageFilter("192.168.100.1"))

logfile = logging.FileHandler("logfile.log")
logfile.setLevel(logging.DEBUG)
logfile.setFormatter(fmt)

# logger
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(stderr)
log.addHandler(logfile)
log.addFilter(AddIPFilter())

## messages
log.debug("Сообщение уровня debug")
log.debug("Сообщение уровня debug 192.168.100.1")
log.debug("Сообщение уровня debug 192.168.100.2")
log.info("Сообщение уровня info 192.168.100.1")
log.warning("Сообщение уровня warning")

