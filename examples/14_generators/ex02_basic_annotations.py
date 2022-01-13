from typing import Iterator, Generator


def generate_nums(number: int) -> Iterator[int]:
    print('Start of generation')
    yield number
    print('Next number')
    yield number + 1
    print('The end')



