import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.WARNING)
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)
console.setFormatter(formatter)

logger.addHandler(console)

## messages
logger.debug("Сообщение уровня debug %s", "SOS")
logger.info("Сообщение уровня info")
logger.warning("Сообщение уровня warning")
logger.error("Сообщение уровня error")
