from pprint import pprint

DEVICE_TYPE_CLASS_MAP = {}

def register(cls):
    DEVICE_TYPE_CLASS_MAP[cls.device_type] = cls.__name__
    return cls


class CiscoIosBase:
    pass


@register
class CiscoSSH(CiscoIosBase):
    device_type = "cisco_ios"

    def __init__(self, ip, user, password):
        pass


@register
class JuniperSSH:
    device_type = "juniper"

    def __init__(self, ip, user, password):
        pass

pprint(DEVICE_TYPE_CLASS_MAP)
