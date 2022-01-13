from __future__ import annotations
import time
import telnetlib
import re
from typing import Optional, Dict, Any

import yaml


class CiscoTelnet:
    def __init__(
        self,
        host: str,
        username: str,
        password: str,
        secret: Optional[str] = None,
        disable_paging: bool = True,
        read_timeout: int = 5,
        encoding: str = "utf-8",
    ) -> None:
        self.host = host
        self.username = username
        self.prompt = ">"
        self.read_timeout = read_timeout
        self.encoding = encoding
        self.hostname = ""

        self._telnet = telnetlib.Telnet(host)
        self._read_until("Username")
        self._write_line(username)
        self._read_until("Password")
        self._write_line(password)

        match_index, match_obj, output = self._telnet.expect(
            [b">", b"#"], timeout=self.read_timeout
        )
        if not match_obj:
            raise ValueError("Cisco prompt not found")
        match_host = re.search(r"(\S+)[#>]", output.decode(self.encoding))
        if match_host:
            self.hostname = match_host.group(1)

        if match_index == 0 and secret:
            self._write_line("enable")
            self._read_until("Password")
            self._write_line(secret)
            self._read_until("#")
            self.prompt = "#"
        elif match_index == 1:
            self.prompt = "#"
        if disable_paging:
            self._write_line("terminal length 0")
            self._read_until(self.prompt)

    def _read_until(self, line: str) -> str:
        output = self._telnet.read_until(
            line.encode(self.encoding), timeout=self.read_timeout
        )
        return output.decode(self.encoding).replace("\r\n", "\n")

    def _write_line(self, line: str) -> None:
        self._telnet.write(f"{line}\n".encode(self.encoding))
        return None

    def send_show_command(self, command: str) -> str:
        self._write_line(command)
        command_output = self._read_until(self.prompt)
        return command_output

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._telnet.close()


if __name__ == "__main__":
    r1_params: Dict[str, Any] = {
        "host": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    with CiscoTelnet(**r1_params) as r1:
        print(r1.send_show_command("sh clock"))
        print(r1.send_show_command("sh ip int br"))
        print(r1.send_show_command("sh run | i hostname"))
