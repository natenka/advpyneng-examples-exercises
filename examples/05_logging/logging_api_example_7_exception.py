import logging
from netmiko_func import send_show_command, device_params

logger = logging.getLogger("superscript")
logger.setLevel(logging.DEBUG)

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    "%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt="%H:%M:%S"
)
console.setFormatter(formatter)

logger.addHandler(console)

logger.debug("Before exception")

try:
    2 + "test"
except TypeError as err:
    # print(err)
    logger.exception("Возникла ошибка")

logger.debug("After exception")
