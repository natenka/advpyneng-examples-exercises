from task_19_2 import send_config_commands


def test_function_1(device_example, device_connection):
    command = "logging 1.1.1.1"
    result = send_config_commands(device_example, command)
    assert command in result


def test_function_2(device_example, device_connection):
    command = "logging 1.1.1.1"
    result = send_config_commands(device_example, command)
    assert "%" not in result, "При выполнении команды возникла ошибка"
