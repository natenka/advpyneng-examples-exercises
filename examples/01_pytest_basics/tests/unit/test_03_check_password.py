from ex03_check_password_function import check_passwd
import pytest


@pytest.mark.parametrize(
    ("user", "passwd", "min_len", "result"),
    [
        ("user1", "123456", 4, True),
        ("user1", "123456", 8, False),
        ("user1", "123456", 6, True),
    ],
)
def test_min_len_param(user, passwd, min_len, result):
    assert check_passwd(user, passwd, min_length=min_len) == result
