from dataclasses import dataclass, field
from typing import List
from datetime import datetime

class AccessDenied(Exception):
    pass


@dataclass(order=True)
class Permission:
    name: str = field(compare=False)
    level: int


user = Permission("user", 10)
admin = Permission("admin", 50)


@dataclass(order=True)
class User:
    username: str
    password: str = field(repr=False, compare=False)
    permission: Permission
    sessions: List[str] = field(default_factory=list)


def data1(user, permission=admin):
    if user.permission < permission:
        raise AccessDenied("У вас недостаточно прав для просмотра")
    print("SECRET DATA")


def login(user):
    user.sessions.append(str(datetime.now()))


u1 = User("user1", "password1", user)
u2 = User("user2", "password1", user)
u3 = User("user3", "password3", admin)


