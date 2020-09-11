from pprint import pprint
from netmiko import ConnectHandler
from textfsm import clitable
from typing import Dict, Union, List


def send_and_parse_show_command(
    device_dict: Dict[str, str],
    command: str,
    index_file: str = "index",
    templ_path: str = "templates",
) -> Union[str, List[Dict[str, str]]]:
    attributes = {"Command": command, "Vendor": device_dict["device_type"]}
    with ConnectHandler(**device_dict) as ssh:
        ssh.enable()
        command_output = ssh.send_command(command)

    try:
        cli_table = clitable.CliTable(index_file, templ_path)
        cli_table.ParseCmd(command_output, attributes)
        return [dict(zip(cli_table.header, row)) for row in cli_table]
        # проверка вложенных значений
        # return [list(zip(cli_table.header, row)) for row in cli_table]
    except clitable.CliTableError:
        return command_output


if __name__ == "__main__":
    device_params = {
        "device_type": "cisco_ios",
        "host": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    result = send_and_parse_show_command(device_params, "sh ip int br")
    # result = send_and_parse_show_command(device_params, 'sh ip route ospf')
    pprint(result, width=100)
