from task_19_1 import send_show_command


def test_function_1(device_example, device_connection):
    result = send_show_command(device_example, "sh ip int br")
    assert device_example["host"] in result


def test_function_2(device_example, device_connection):
    correct_result = device_connection.send_command("sh ip int br")
    result = send_show_command(device_example, "sh ip int br")
    assert result == correct_result
