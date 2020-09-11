# -*- coding: utf-8 -*-
"""
Задание 7.2a

Изменить функцию count_total из задания 7.2.
После вызова функции count_total, должна быть доступна возможность обращаться к
атрибуту buy и передавать ему аргумент - число. Как результат должна возвращаться
текущая сумма чисел.

Пример использования функции count_total:

In [2]: books = count_total()

In [3]: books.buy(25)
Out[3]: 25

In [4]: books.buy(15)
Out[4]: 40

In [5]: books.buy(115)
Out[5]: 155

In [6]: books.buy(25)
Out[6]: 180

In [7]: toys = count_total()

In [8]: toys.buy(67)
Out[8]: 67

In [9]: toys.buy(17)
Out[9]: 84

In [10]: toys.buy(24)
Out[10]: 108
"""
