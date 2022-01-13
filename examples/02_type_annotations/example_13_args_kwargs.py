from typing import Tuple, Dict

def func(
    user: str, *args: str, **kwargs: float
) -> None:
    print(user, args, kwargs)



if __name__ == "__main__":
    func("user1", "pass2", "test", timeout=1.0, close_timeout=10.0)
