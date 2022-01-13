class Password:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        # print(f"__get__ {self=} {instance=} {cls=}")
        return "*" * 10

    def __set__(self, instance, new_password):
        # print(f"__set__ {self=} {instance=} {value=}")
        if len(new_password) < 8:
            raise ValueError("Пароль слишком короткий.")
        instance.__dict__[self.name] = new_password


class User:
    password = Password("_password")

    def __init__(self, username, password):
        self.password = password


if __name__ == "__main__":
    user1 = User("user1", "sdfsadfsdf")
    print(user1.password)
    user2 = User("user2", "sdfs")
