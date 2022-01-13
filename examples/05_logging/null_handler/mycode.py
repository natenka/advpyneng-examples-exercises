import logging
from base_ssh_class import BaseSSH
from base_functions import send_show
import yaml


logging.getLogger("paramiko").setLevel(logging.INFO)
logging.basicConfig(level=logging.DEBUG)


if __name__ == "__main__":
    with open("devices.yaml") as f:
        devices = yaml.safe_load(f)
    with BaseSSH("192.168.100.1", "cisco", "cisco") as r1:
        print(r1.send_show_command("sh clock"))
    print(send_show(device[0], "sh clock"))
