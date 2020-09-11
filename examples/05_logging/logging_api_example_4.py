import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

### stderr
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "{asctime} - {name} - {levelname} - {message}", datefmt="%H:%M:%S", style="{"
)
console.setFormatter(formatter)

logger.addHandler(console)

### File
logfile = logging.FileHandler("logfile3.log")
logfile.setLevel(logging.WARNING)
formatter = logging.Formatter("{asctime} - {name} - {levelname} - {message}", style="{")
logfile.setFormatter(formatter)

logger.addHandler(logfile)

## messages
logger.debug("Сообщение уровня debug")
logger.info("Сообщение уровня info")
logger.warning("Сообщение уровня warning")
