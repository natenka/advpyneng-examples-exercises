from functools import total_ordering

class IPAddress:
    ip_version = 4

    def __init__(self, ip):
        if isinstance(ip, int):
            bin_str = f"{ip:032b}"
            self.ip = ".".join(
                [str(int(bin_str[i: i + 8], 2)) for i in [0,8,16,24]]
            )
        elif isinstance(ip, str):
            self.ip = ip
        else:
            raise ValueError

    def __str__(self):
        return self.ip

    def __repr__(self):
        # "IPAddress('10.1.1.1')"
        return f"{type(self).__name__}('{self.ip}')"

    def __lt__(self, other):
        print("__lt__")
        if not isinstance(other, IPAddress):
            raise TypeError(
                f"'<' not supported between instances of "
                f"'{type(self).__name__}' and '{type(other).__name__}'"
            )
        return int(self) < int(other)

    def __eq__(self, other):
        print("__eq__")
        if not isinstance(other, IPAddress):
            raise TypeError(
                f"'+' not supported between instances of "
                f"'{type(self).__name__}' and '{type(other).__name__}'"
            )
        return int(self) == int(other)

    def __int__(self):
        print("__int__")
        bin_ip = "".join([
            f"{int(octet):08b}" for octet in self.ip.split(".")
        ])
        return int(bin_ip, 2)

    def __add__(self, other):
        print("__add__")
        if not isinstance(other, int):
            raise TypeError(
                f"unsupported operand type(s) for +: "
                f"'{type(self).__name__}' and '{type(other).__name__}'"
            )
        # return IPAddress(int(self) + other)
        return type(self)(int(self) + other)

    def __radd__(self, other):
        print("__radd__")
        return self + other
