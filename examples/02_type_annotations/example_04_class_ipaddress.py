# from __future__ import annotations
from pprint import pprint


class IPAddress:
    def __init__(self, ip: str, mask: int):
        self.ip = ip
        self.mask = mask

    def __repr__(self):
        return f"IPAddress({self.ip}/{self.mask})"

    def __add__(self, other) -> "IPAddress":
        pass


pprint(IPAddress.__add__.__annotations__)
pprint(IPAddress.__init__.__annotations__)
