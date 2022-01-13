from typing import Callable


def multiply(num1: int) -> Callable[[int], int]:
    def inner(num2: int) -> int:
        return num1 * num2
    return inner
