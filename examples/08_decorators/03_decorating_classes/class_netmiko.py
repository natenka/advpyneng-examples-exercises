CLASS_MAP = {}


def register(cls):
    CLASS_MAP[cls.device_type] = cls
    return cls


#CiscoIos = register(CiscoIos)

@register
class CiscoIos:
    device_type = "cisco_ios"

    def __init__(self, hostname, username, password):
        pass


@register
class CiscoXR:
    device_type = "cisco_xr"

    def __init__(self, hostname, username, password):
        pass
