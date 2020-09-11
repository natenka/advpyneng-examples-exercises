import pytest
from check_password_function import check_passwd


@pytest.mark.parametrize(
    "username,password,min_length,result",
    [("nata", "12345", 3, True), ("nata", "12345nata", 3, False)],
)
def test_password_min_length(username, password, min_length, result):
    assert result == check_passwd(username, password, min_length=min_length)
