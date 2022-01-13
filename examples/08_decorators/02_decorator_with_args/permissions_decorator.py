from functools import wraps


class User:
    def __init__(self, username, permissions=None):
        self.username = username
        self.permissions = permissions

    def has_permissions(self, permission):
        return permission in self.permissions


class AccessDenied(Exception):
    pass


def permission_required(permission):
    def decorator(func):
        @wraps(func)
        def inner(*args, **kwargs):
            if not current_user.has_permissions(permission):
                raise AccessDenied("You shall not pass!!!")
            return func(*args, **kwargs)

        return inner

    return decorator
