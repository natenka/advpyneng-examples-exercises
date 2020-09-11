import re
from netmiko import ConnectHandler


def send_config_commands(device, config_commands, verbose=True):
    good_commands = {}
    bad_commands = {}
    error_message = 'Команда "{}" выполнилась с ' 'ошибкой "{}" на устройстве {}'
    regex = "% (?P<errmsg>.+)"

    if verbose:
        print("Подключаюсь к {}...".format(device["host"]))
    with ConnectHandler(**device) as ssh:
        ssh.enable()
        for command in config_commands:
            result = ssh.send_config_set(command, exit_config_mode=False)
            error_in_result = re.search(regex, result)
            if error_in_result:
                print(
                    error_message.format(
                        command, error_in_result.group("errmsg"), ssh.host
                    )
                )
                bad_commands[command] = result
            else:
                good_commands[command] = result
            ssh.exit_config_mode()
    return good_commands, bad_commands
