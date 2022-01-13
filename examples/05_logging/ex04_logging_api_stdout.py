import sys
import logging
from rich import inspect


fmt = logging.Formatter("{asctime} {name} {levelname} {message}", style="{")
stderr = logging.StreamHandler(sys.stdout)
stderr.setLevel(logging.INFO)
stderr.setFormatter(fmt)

# logger
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
log.addHandler(stderr)

## messages
log.debug("Сообщение уровня debug")
log.info("Сообщение уровня info")
log.warning("Сообщение уровня warning")
