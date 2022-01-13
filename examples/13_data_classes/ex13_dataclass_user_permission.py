from dataclasses import dataclass, field
from typing import List
from datetime import datetime


class AccessDenied(Exception):
    pass


@dataclass(order=True)
class Permission:
    name: str = field(compare=False)
    level: int


@dataclass(order=True)
class User:
    username: str
    password: str = field(repr=False)
    permission: Permission
    sessions: List[str] = field(default_factory=list)

user = Permission("user", 10)
admin = Permission("admin", 50)

def check_permission(user, required_permission=admin):
    if user.permission < required_permission:
        raise AccessDenied("Недостаточно прав")
    print(42)


def login(user):
    user.sessions.append(str(datetime.now()))

u1 = User("user1", "password1", user)
u2 = User("user2", "password2", admin)

