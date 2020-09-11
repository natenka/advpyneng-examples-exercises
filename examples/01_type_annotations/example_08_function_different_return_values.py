from pprint import pprint
from netmiko import (
    ConnectHandler,
    NetMikoAuthenticationException,
    NetMikoTimeoutException,
)
from typing import Union, Dict, Optional


def send_show_command(device_dict: Dict[str, str], command: str) -> Union[str, None]:
    # def send_show_command(device_dict: Dict[str, str],
    #                      command: str
    #                     ) -> Optional[str]:
    try:
        with ConnectHandler(**device_dict) as ssh:
            ssh.enable()
            command_output = ssh.send_command(command)
        return command_output
    except (NetMikoAuthenticationException, NetMikoTimeoutException) as error:
        print(error)
        return None


if __name__ == "__main__":
    device_params = {
        "device_type": "cisco_ios",
        "host": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    result = send_show_command(device_params, "sh ip int br")
    result + "test"
    # result = send_show_command(device_params, 'sh ip route ospf')
    pprint(result, width=100)
