from typing import Optional, Iterable


def check_passwd(
    username: str,
    password: str,
    min_length: int = 8,
    check_username: bool = True,
    forbidden_symbols: Optional[Iterable[str]] = None,
) -> bool:
    if len(password) < min_length:
        print("Пароль слишком короткий")
        return False
    elif check_username and username in password:
        print("Пароль содержит имя пользователя")
        return False
    elif forbidden_symbols and set(forbidden_symbols) & set(password):
        return False
    else:
        print(f"Пароль для пользователя {username} прошел все проверки")
        return True


if __name__ == "__main__":
    check_passwd("nata", "12345", min_length=3)
    check_passwd("nata", "12345nata", min_length=3, forbidden_symbols=["@"])
    check_passwd("nata", "12345nata", min_length=3, check_username=False)
    check_passwd("nata", "12345nata", min_length=3, check_username=True)
