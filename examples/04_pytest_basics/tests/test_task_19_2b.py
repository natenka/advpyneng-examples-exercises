from task_19_2b import send_config_commands


def test_function_1(device_example, device_connection):
    command = "logging 1.1.1.1"
    correct, failed = send_config_commands(device_example, [command])
    assert command in correct and "%" not in correct[command]


def test_function_2(capsys, device_example, device_connection):
    error, command = "Invalid input detected", "logging 0255.255.1"
    result = send_config_commands(device_example, [command])
    stdout, stderr = capsys.readouterr()
    assert error in stdout
