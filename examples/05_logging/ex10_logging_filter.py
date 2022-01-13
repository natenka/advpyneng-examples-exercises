import logging

from logging_filters import LevelFilter, MessageFilter


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger.addFilter(LevelFilter(logging.DEBUG))
logger.addFilter(MessageFilter("test"))

### stderr
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
# console.addFilter(LevelFilter(logging.DEBUG))
# console.addFilter(MessageFilter("test"))
formatter = logging.Formatter(
    "{asctime} - {name} - {levelname} - {message}", datefmt="%H:%M:%S", style="{"
)
console.setFormatter(formatter)

logger.addHandler(console)

### File
logfile = logging.FileHandler("logfile3.log")
logfile.setLevel(logging.DEBUG)

formatter = logging.Formatter("{asctime} - {name} - {levelname} - {message}", style="{")
logfile.setFormatter(formatter)

logger.addHandler(logfile)

## messages
logger.debug("Сообщение уровня debug")
logger.debug("Сообщение уровня debug. test1")
logger.debug("Сообщение уровня debug. test2")
logger.info("Сообщение уровня info")
logger.warning("Сообщение уровня warning")
