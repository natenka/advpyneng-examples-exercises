# from typing import Union
#
#
# def my_summ(a: Union[str, int], b: Union[str, int]) -> Union[str, int]:
#    return a + b


from typing import overload, Union, TypeVar

StrOrInt = TypeVar("StrOrInt", str, int)


@overload
def my_summ(a: str, b: str) -> str:
    pass


@overload
def my_summ(a: int, b: int) -> int:
    pass


def my_summ(a: StrOrInt, b: StrOrInt) -> StrOrInt:
    return a + b
