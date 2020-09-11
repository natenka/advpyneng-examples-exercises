import logging

mylogger = logging.getLogger("My Script")
# mylogger = logging.getLogger(__name__)

## messages
mylogger.debug("Сообщение уровня debug")
mylogger.info("Сообщение уровня info")
mylogger.warning("Сообщение уровня warning")
