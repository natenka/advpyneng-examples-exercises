from functools import wraps


class User:
    def __init__(self, username, permissions=None):
        self.username = username
        self.permissions = permissions

    def has_permission(self, permission):
        return permission in self.permissions

    def __repr__(self):
        return f"User(username='{self.username}')"


natasha = User('nata', ['admin', 'user'])
oleg = User('oleg', ['user'])


class AccessDenied(Exception):
    pass


current_user = natasha


def permission(permission_name):
    print("Вызываю permission")
    def decorator(func):
        print("Выполняем декорацию")
        def inner(*args, **kwargs):
            print(current_user)
            if not current_user.has_permission(permission_name):
                raise AccessDenied("У пользователя нет прав просмотра")
            return func(*args, **kwargs)
        return inner
    return decorator

