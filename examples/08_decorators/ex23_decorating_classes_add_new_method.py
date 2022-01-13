from rich import print as rprint

def _pprint(self, methods=False):
    attrs = vars(self)
    rprint(attrs)
    all_methods = vars(type(self))
    methods_dict = {
        name: method
        for name, method in all_methods.items()
        if not name.startswith("__") and callable(method)
    }
    if methods:
        rprint(methods_dict)


def add_pprint(cls):
    cls.pprint = _pprint
    return cls


@add_pprint
class IPAddress:
    def __init__(self, ip, mask):
        self.ip = ip
        self.mask = mask

    def __repr__(self):
        return f"IPAddress({self.ip}/{self.mask})"

    def bin_mask(self):
        return "1" * self.mask + "0" * (32 - self.mask)

