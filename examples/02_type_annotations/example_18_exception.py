from typing import Dict, Union, List, Any


def summ(x: int, y: int) -> int:
    if isinstance(x, int) and isinstance(y, int):
        return x + y
    else:
        raise ValueError('Аргументы должны быть числами')
