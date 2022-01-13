

class Password:
    def __set_name__(self, owner, attr_name):
        print(f"set_name {owner=} {attr_name=}")
        self.tuzik = attr_name

    def __get__(self, instance, cls):
        print(f"__get__  {instance=} {cls=}")
        raise AttributeError

    def __set__(self, instance, value):
        print(f"__set__  {instance=} {value=}")
        if len(value) < 6:
            raise ValueError("Пароль слишком короткий")
        instance.__dict__[self.tuzik] = value


class User:
    password = Password()

    def __init__(self, user, password):
        self.password = password
