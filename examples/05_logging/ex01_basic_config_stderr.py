import logging

logging.basicConfig(level=logging.DEBUG)

vara = "TEST"
varb = "dhcp_snooping.db"

logging.debug("Сообщение уровня debug %s", str(globals()))
logging.info("Сообщение уровня info {}".format(globals()))
logging.warning(f"Сообщение уровня warning {globals()}")


