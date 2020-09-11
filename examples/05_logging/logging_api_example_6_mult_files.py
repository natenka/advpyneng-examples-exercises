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

if __name__ == "__main__":
    logger.debug("Before function")
    send_show_command(device_params, "sh ip int br")
    logger.debug("After function")

logger.setLevel(logging.WARNING)

if __name__ == "__main__":
    logger.warning("Before function")
    send_show_command(device_params, "sh ip int br")
    logger.warning("After function")
