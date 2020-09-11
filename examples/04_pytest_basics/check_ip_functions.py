import ipaddress


def check_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError as err:
        return False


def test_check_ip():
    assert (
        check_ip("10.1.1.1") == True
    ), "При правильном IP, функция должна возвращать True"
    assert (
        check_ip("500.1.1.1") == False
    ), "Если адрес неправильный, функция должна возвращать False"


if __name__ == "__main__":
    result = check_ip("10.1.1.1")
    print("Function result:", result)
