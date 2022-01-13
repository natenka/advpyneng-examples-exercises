
def create_init(cls):
    attrs = list(cls.__annotations__.keys())
    init = f"def __init__(self, {', '.join(attrs)}):\n"
    for attr in attrs:
        init += f"    self.{attr} = {attr}\n"
    print(init)
    exec(init)
    init_method = locals()["__init__"]
    return init_method


def create_repr(cls):
    attrs = list(cls.__annotations__.keys())
    repr_str = ", ".join([f"{attr}='{{self.{attr}}}'" for attr in attrs])
    reprm = (
        f"def __repr__(self):\n"
        f'   return self.__class__.__name__ + f"({repr_str})"'
    )
    print(reprm)
    exec(reprm)
    repr_method = locals()["__repr__"]
    return repr_method


def my_dataclass(cls):
    print("Декорируем класс")
    cls.__init__ = create_init(cls)
    cls.__repr__ = create_repr(cls)
    return cls

@my_dataclass
class IPAddress:
    ip: str
    mask: int

@my_dataclass
class Book:
    title: str
    price: int
    quantity: int

