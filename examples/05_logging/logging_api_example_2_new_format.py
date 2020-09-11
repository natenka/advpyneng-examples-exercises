import logging

logger = logging.getLogger("__name__")
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "{asctime} - {name} - {levelname} - {message}", datefmt="%H:%M:%S", style="{"
)
console.setFormatter(formatter)

logger.addHandler(console)

## messages
logger.debug("Сообщение уровня debug: %s", "SOS")
logger.info("Сообщение уровня info")
logger.warning("Сообщение уровня warning")
