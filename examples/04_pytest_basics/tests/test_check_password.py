from check_password_function import check_passwd


def test_password_min_length():
    print("Проверяем пароль")
    assert check_passwd("nata", "12345", min_length=3)
    assert not check_passwd("nata", "12345nata", min_length=3)


def test_password_contains_username():
    assert check_passwd("nata", "12345nata", min_length=3, check_username=False)
    assert not check_passwd("nata", "12345nata", min_length=3, check_username=True)
    # assert not check_passwd('nata', '12345NATA', min_length=3, check_username=True), "Если в пароле присутствует имя пользователя в любом регистре, проверка не должна пройти"


def test_password_default_values():
    assert not check_passwd("nata", "12345")
    assert not check_passwd("nata", "12345nata")
    assert check_passwd("nata", "12345dsfsda")
