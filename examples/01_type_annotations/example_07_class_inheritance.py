import paramiko
import time
from typing import Union, List


class BaseSSH:
    def __init__(self, ip: str, username: str, password: str) -> None:
        self.ip = ip
        self.username = username
        self.password = password
        ####

    def send_config_commands(self, commands: Union[str, List[str]]) -> str:
        if isinstance(commands, str):
            commands = [commands]
        for command in commands:
            time.sleep(0.5)
        return "result"


class CiscoSSH(BaseSSH):
    def __init__(
        self,
        ip: str,
        username: str,
        password: str,
        secret: str,
        disable_paging: bool = True,
    ) -> None:
        super().__init__(ip, username, password)

    def send_config_commands(self, commands: Union[str, List[str]]) -> str:
        # send....(conf t)
        return "result"
