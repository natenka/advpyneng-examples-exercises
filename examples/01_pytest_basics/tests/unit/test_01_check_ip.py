import pytest

from ex01_check_ip_function import check_ip


def test_check_ip():
    correct_ip_list = ["10.1.1.1", "224.1.1.1", "0.0.0.0"]
    for ip in correct_ip_list:
        assert check_ip(ip) == True
    wrong_ip_list = ["500.1.1.1", "50.1.1", "a", 100, []]
    for ip in wrong_ip_list:
        assert check_ip(ip) == False


@pytest.mark.parametrize("ip", ["10.1.1.1", "224.1.1.1", "0.0.0.0"])
def test_check_ip_correct(ip):
    assert check_ip(ip) == True


@pytest.mark.parametrize("ip", ["500.1.1.1", "50.1.1", "a", 100, []])
def test_check_ip_wrong(ip):
    assert check_ip(ip) == False
