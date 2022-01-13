from pprint import pprint
from asyncssh import SSHClientConnectionOptions
import yaml


with open("devices_scrapli.yaml") as f:
    devices = yaml.safe_load(f)

options = SSHClientConnectionOptions()
options.encryption_algs.append(b"aes256-cbc")
devices = [{**device, "transport_options": options} for device in devices]
# pprint(devices)
