from scrapli import Scrapli
from scrapli.exceptions import ScrapliException, ScrapliAuthenticationFailed
import yaml


class MyException(Exception):
    pass


def send_show(device, show):
    try:
        with Scrapli(**device) as ssh:
            reply = ssh.send_command(show)
            return reply.result
    except ScrapliAuthenticationFailed:
        raise MyException("TEST")
    except ScrapliException as err:
        print(err)



if __name__ == "__main__":
    with open("devices_scrapli.yaml") as f:
        devices = yaml.safe_load(f)
    r1 = devices[0]
    print(send_show(r1, "sh clock"))
