from __future__ import annotations
import telnetlib
import time
from typing import List, Dict, Union, Optional


class CiscoTelnet:
    def __init__(
        self,
        ip: str,
        username: str,
        password: str,
        enable_password: Optional[str] = None,
        disable_paging: bool = True,
    ) -> None:
        self.ip = ip
        self._telnet = telnetlib.Telnet(ip)
        self._telnet.read_until(b"Username:")
        self._telnet.write(username.encode("utf-8") + b"\n")

        self._telnet.read_until(b"Password:")
        self._telnet.write(password.encode("utf-8") + b"\n")
        if enable_password:
            self._telnet.write(b"enable\n")
            self._telnet.read_until(b"Password:")
            self._telnet.write(enable_password.encode("utf-8") + b"\n")
        if disable_paging:
            self._telnet.write(b"terminal length 0\n")
        time.sleep(1)
        self._telnet.read_very_eager()

    def send_show_command(self, command: str) -> str:
        self._telnet.write(command.encode("utf-8") + b"\n")
        output = self._telnet.read_until(b"#").decode("utf-8")
        return output

    def send_config_commands(self, commands: Union[List[str], str]) -> str:
        if isinstance(commands, str):
            commands = [commands]
        output = ""
        commands = ["conf t", *commands, "end"]
        for command in commands:
            self._telnet.write(command.encode("utf-8") + b"\n")
            output += self._telnet.read_until(b"#").decode("utf-8")
        return output

    def close(self) -> None:
        self._telnet.close()

    def __enter__(self) -> CiscoTelnet:
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        self._telnet.close()


if __name__ == "__main__":
    with CiscoTelnet("192.168.100.1", "cisco", "cisco", "cisco") as r1:
        print(r1.send_show_command("sh ip int br"))
        print(
            r1.send_config_commands(
                ["int lo55", "ip address 10.5.5.55 255.255.255.255"]
            )
        )
