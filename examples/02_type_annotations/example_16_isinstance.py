from netmiko import ConnectHandler
from typing import Dict, Union, Iterable, Any


def send_show_commands(
    device_params: Dict[str, Any], commands: Union[str, Iterable[str]]
) -> Dict[str, str]:
    result = {}
    # if type(commands) == str:
    if isinstance(commands, str):
        commands = [commands]
    with ConnectHandler(**device_params) as ssh:
        ssh.enable()
        for command in commands:
            output = ssh.send_command(command)
            result[command] = output
    return result
