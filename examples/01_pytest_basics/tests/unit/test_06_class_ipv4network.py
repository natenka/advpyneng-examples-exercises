from collections.abc import Iterable
import pytest
from ex06_class_ipv4network import IPv4Network


def test_attributes_created():
    """
    Проверяем, что у объекта есть атрибуты:
        network, mask, bin_mask
    """
    net = IPv4Network("100.7.1.0/26")
    assert getattr(net, "network", None) != None, "Атрибут не найден"
    assert getattr(net, "mask", None) != None, "Атрибут не найден"
    assert getattr(net, "bin_mask", None) != None, "Атрибут не найден"


def test_attributes():
    """Проверяем значения атрибутов"""
    net = IPv4Network("10.1.1.0/29")
    assert net.network == "10.1.1.0/29"
    assert net.mask == 29
    assert net.bin_mask == "11111111111111111111111111111000"


def test_hosts():
    """Проверяем работу метода hosts"""
    net = IPv4Network("100.7.1.0/26")
    assert type(net.hosts()) == list, "Метод hosts должен возвращать список"
    assert len(net.hosts()) == 62, "В данной сети должно быть 62 хоста"


def test_repr():
    """Проверяем работу метода __repr__"""
    net = IPv4Network("192.168.1.0/26")
    assert repr(net) == "Network('192.168.1.0/26')"


def test_len():
    """Проверяем работу метода __len__"""
    net = IPv4Network("192.168.1.0/26")
    assert len(net) == 62


def test_iter():
    """Проверяем что IPv4Network итерируемый объект"""
    net = IPv4Network("192.168.1.0/26")
    net_iterator = iter(net)
    assert next(net_iterator) == "192.168.1.1"
    assert isinstance(net, Iterable)
