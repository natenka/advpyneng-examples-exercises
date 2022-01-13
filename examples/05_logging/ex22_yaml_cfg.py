import logging
import logging.config
import yaml

CFG_PATH = "/home/vagrant/repos/bonus/pyneng-online-bonus/examples/06_logging/"

# create logger
logger = logging.getLogger(__name__)

# read config
with open(CFG_PATH + "log_config.yml") as f:
    log_config = yaml.safe_load(f)

logging.config.dictConfig(log_config)

## messages
logger.debug("Сообщение уровня debug %s", "SOS")
logger.info("Сообщение уровня info")
logger.warning("Сообщение уровня warning")
