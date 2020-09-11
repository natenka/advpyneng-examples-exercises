CLASS_MAPPER_MAP = {}


def register_class(cls):
    CLASS_MAPPER_MAP[cls.device_type] = cls
    return cls


class CiscoIosBase:
    pass


@register_class
class CiscoSSH(CiscoIosBase):
    device_type = "cisco_ios"

    def __init__(self, ip, user, password):
        pass


@register_class
class JuniperSSH:
    device_type = "juniper"
