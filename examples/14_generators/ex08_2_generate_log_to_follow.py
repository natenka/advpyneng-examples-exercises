import logging
import random
import time

import yaml
from scrapli import Scrapli
from scrapli.exceptions import ScrapliException


logging.getLogger("scrapli").setLevel(logging.WARNING)

logging.basicConfig(
    filename="scrapli_example.log",
    format="%(asctime)s %(name)s %(levelname)s: %(message)s",
    level=logging.DEBUG,
)


def send_show(device, show_commands):
    host = device["host"]
    if type(show_commands) == str:
        show_commands = [show_commands]
    cmd_dict = {}
    logging.info(f">>> Connecting to {host}")
    try:
        with Scrapli(**device) as ssh:
            for cmd in show_commands:
                reply = ssh.send_command(cmd)
                cmd_dict[cmd] = reply.result
        logging.info(f"<<< Received output from {host}")
        return cmd_dict
    except ScrapliException as error:
        logging.error(f"{error} {host}")


def main():
    commands = [
        "sh clock",
        "sh ip int br | i Loopback0",
        "sh version | i uptime",
        "sh run | i hostname",
    ]
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    while True:
        for dev in devices:
            logging.debug(send_show(dev, random.choice(commands)))
            time.sleep(1)


if __name__ == "__main__":
    main()
