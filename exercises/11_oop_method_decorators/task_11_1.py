# -*- coding: utf-8 -*-
"""
Задание 11.1

Скопировать класс IPv4Network из задания 9.1.
Переделать класс таким образом, чтобы запись значения в переменную hosts
была запрещена.


Пример создания экземпляра класса:
In [1]: net1 = IPv4Network('8.8.4.0/29')

In [2]: net1.hosts
Out[2]: ('8.8.4.1', '8.8.4.2', '8.8.4.3', '8.8.4.4', '8.8.4.5', '8.8.4.6')

Запись переменной:

In [6]: net1.hosts = 'test'
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-6-c98e898835e1> in <module>
----> 1 net1.hosts = 'test'

AttributeError: can't set attribute

"""
