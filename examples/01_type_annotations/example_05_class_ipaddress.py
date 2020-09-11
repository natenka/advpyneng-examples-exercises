class IPAddress:
    def __init__(self, ip: str, mask: int) -> None:
        self.ip = ip
        self.mask = mask

    def __repr__(self) -> str:
        return f"IPAddress({self.ip}/{self.mask})"
