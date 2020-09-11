from class_ipv4_network import IPv4Network
import inspect
from common_functions import check_attr_or_method
import pytest


def test_class_attrs():
    net1 = IPv4Network("10.1.1.0/24")
    check_attr_or_method(net1, attr="address")
    check_attr_or_method(net1, attr="mask")
    check_attr_or_method(net1, attr="allocated")


def test_class_method():
    net1 = IPv4Network("10.1.1.0/24")
    check_attr_or_method(net1, method="hosts")
    check_attr_or_method(net1, method="allocate")
    check_attr_or_method(net1, method="unassigned")


def test_class_return_types():
    net1 = IPv4Network("10.1.1.0/24")
    assert type(net1.allocated) == tuple, "allocated должен быть кортежем"
    assert type(net1.hosts()) == tuple, "hosts должен возвращать кортеж"


def test_class():
    net1 = IPv4Network("10.1.1.0/24")
    assert len(net1.allocated) == 0, "По умолчанию allocated пустой кортеж"
    assert len(net1.hosts()) == 254
    net1.allocate("10.1.1.1")
    net1.allocate("10.1.1.8")
    net1.allocate("10.1.1.11")
    with pytest.raises(ValueError):
        net1.allocate("10.2.2.11")  ###

    assert len(net1.allocated) == 3
