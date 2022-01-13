from typing import List, Union, Any
from netmiko import CiscoIosBase


ip_list: List[Union[str, int]] = []
ip_list.append("10.1.1.1")
ip_list.append(4)


def func(*args: Union[str, int]):
    return sum(args)


class MyNetmiko(CiscoIosBase):
    def send_command(self, command: str, *args: Any, **kwargs: Any):
        print(command)
        super().send_command(command, *args, **kwargs)
