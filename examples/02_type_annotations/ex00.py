import ipaddress
from typing import Iterable, Union, List

# python 3.9
# from collections.abc import Iterable


def sum_numbers(
    number_sequence: Iterable[Union[int, float]]
) -> Union[int, float]:
    return sum(number_sequence)


def check_ip(ip: List[int]) -> bool:
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError as err:
        return False


if __name__ == "__main__":
    print(sum_numbers([1, 2]))
    print(sum_numbers((1, 2)))
    print(sum_numbers((1.5, 2.2)))
    print(sum_numbers((1.5, 2)))
    # аннотация без создания переменной
    test: bool
    # print(test) # error
