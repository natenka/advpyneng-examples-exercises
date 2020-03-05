import pytest
import task_5_3
import sys
sys.path.append('..')

from common_functions import check_class_exists, check_attr_or_method


def test_class_created():
    '''Проверяем, что класс создан и что класс создан с помощью dataclass'''
    check_class_exists(task_5_3, 'Book')
    assert hasattr(task_5_3.Book, "__dataclass_params__"), "Класс надо создать с помощью dataclass"


def test_method_to_dict():
    '''Проверка наличия метода to_dict и его работы'''

    book1 = task_5_3.Book('Fluent Python', 20, 100)
    check_attr_or_method(book1, method='to_dict')
    attr_dict = book1.to_dict()

    assert isinstance(attr_dict, dict), "Метод to_dict должен возвращать словарь"
    assert attr_dict == {'title': 'Fluent Python', 'price': 20.0, 'quantity': 100, 'total': 2000.0}

