import logging

logging.basicConfig(filename="mylog2.log", level=logging.DEBUG)

logging.debug("Сообщение уровня debug:\n%s", str(globals()))
logging.info("Сообщение уровня info")
logging.warning("Сообщение уровня warning")
