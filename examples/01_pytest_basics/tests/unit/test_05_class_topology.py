import pytest
from ex05_class_topology import Topology


def test_topology_normalization(topology_with_dupl_links, normalized_topology_example):
    """Проверка удаления дублей в топологии"""
    top_with_data = Topology(topology_with_dupl_links)
    assert len(top_with_data.topology) == len(normalized_topology_example)


def test_method_delete_link_exists(normalized_topology_example, capsys):
    """Проверка работы метода delete_link"""
    norm_top = Topology(normalized_topology_example)
    delete_link_result = norm_top.delete_link(("R3", "Eth0/0"), ("SW1", "Eth0/3"))
    assert delete_link_result == None, "Метод delete_link не должен ничего возвращать"
    assert ("R3", "Eth0/0") not in norm_top.topology, "Соединение не было удалено"


def test_method_delete_link_mirror(normalized_topology_example, capsys):
    """Проверка работы метода delete_link - проверка удаления зеркального линка"""
    norm_top = Topology(normalized_topology_example)
    norm_top.delete_link(("R5", "Eth0/0"), ("R3", "Eth0/2"))
    assert ("R3", "Eth0/2") not in norm_top.topology, "Соединение не было удалено"


def test_method_delete_link_not_exists(normalized_topology_example, capsys):
    """Проверка работы метода delete_link - проверка удаления несуществующего линка"""
    norm_top = Topology(normalized_topology_example)
    norm_top.delete_link(("R8", "Eth0/2"), ("R9", "Eth0/1"))
    out, err = capsys.readouterr()
    link_msg = "Такого соединения нет"
    assert (
        link_msg in out
    ), "При удалении несуществующего соединения, не было выведено сообщение 'Такого соединения нет'"


def test_method__add__(normalized_topology_example):
    """Проверка наличия метода __add__ и его работы"""
    top1 = Topology(normalized_topology_example)
    top1_size_before_add = len(top1.topology)
    top2 = Topology(
        {("R1", "Eth0/4"): ("R7", "Eth0/0"), ("R1", "Eth0/6"): ("R9", "Eth0/0")}
    )
    top2_size_before_add = len(top2.topology)

    top3 = top1 + top2
    assert isinstance(
        top3, Topology
    ), "Метод __add__ должен возвращать новый экземпляр класса Topology"
    assert len(top3.topology) == 8
    assert (
        len(top1.topology) == top1_size_before_add
    ), "После сложения изменился размер первой топологии. Метод __add__ не должен менять исходные топологии"
    assert (
        len(top2.topology) == top2_size_before_add
    ), "После сложения изменился размер второй топологии. Метод __add__ не должен менять исходные топологии"
