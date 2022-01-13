# source https://github.com/python/mypy/issues/2087#issuecomment-587741762

from typing import Protocol, TypeVar, Callable, Optional, cast

F = TypeVar("F", bound=Callable[..., object])


class FunctionWithAttributes(Protocol[F]):
    add_num: Optional[Callable[[], int]]
    sub_num: Optional[Callable[[], int]]
    mul_num: Optional[Callable[[], int]]
    __call__: F


def operations(num1: int, num2: int) -> FunctionWithAttributes[F]:
    operations = cast(FunctionWithAttributes[F], operations)
    def add() -> int:
        return num1 + num2

    def sub() -> int:
        return num1 - num2

    def mul() -> int:
        return num1 * num2

    operations.add_num = add
    operations.sub_num = sub
    operations.mul_num = mul

    return operations
