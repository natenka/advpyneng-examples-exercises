import telnetlib
import time
import netmiko.cisco.cisco_ios.CiscoIos


class CiscoTelnet:
    def __init__(
        self,
        ip,
        username,
        password,
        enable_password=None,
        disable_paging=True,
        strip_command=True,
    ):
        self.ip = ip
        self.telnet = telnetlib.Telnet(ip)
        self.telnet.read_until(b"Username:")
        self.telnet.write(username.encode("ascii") + b"\n")

        self.telnet.read_until(b"Password:")
        self.telnet.write(password.encode("ascii") + b"\n")

        if enable_password:
            self.telnet.write(b"enable\n")
            self.telnet.read_until(b"Password:")
            self.telnet.write(enable_password.encode("ascii") + b"\n")

        if disable_paging:
            self.telnet.write(b"terminal length 0\n")
        time.sleep(0.5)
        self.telnet.read_very_eager()

    def __repr__(self):
        pass


def func():
    pass
