def create_init(cls):
    args = cls.__annotations__.keys()
    args_str = ",".join(args)
    body = ""
    for arg in args:
        body += f"    self.{arg} = {arg}\n"
    function = f"def __init__(self, {args_str}):\n{body}"
    print(function)
    exec(function)
    return locals()["__init__"]


def create_repr(cls):
    args = cls.__annotations__.keys()
    args_value = ", ".join([f"{name}={{self.{name}}}" for name in args])
    body = f'return self.__class__.__qualname__ + f"({args_value})"'
    txt = f"def __repr__(self):\n    {body}"
    print(txt)
    exec(txt)
    return locals()["__repr__"]


def create_dataclass(cls):
    print("создаем dataclass")
    cls.__init__ = create_init(cls)
    cls.__repr__ = create_repr(cls)
    return cls


@create_dataclass
class Book:
    title: str
    price: int
    quantity: int


@create_dataclass
class IPAddress:
    ip: str
    mask: int
