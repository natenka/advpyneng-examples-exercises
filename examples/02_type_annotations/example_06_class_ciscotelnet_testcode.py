from example_04_class_cisco_telnet import CiscoTelnet


if __name__ == "__main__":
    r1_params = {
        "host": "192.168.100.1",
        "username": "cisco",
        "password": "cisco",
        "secret": "cisco",
    }
    with CiscoTelnet(**r1_params) as r1:
        print(r1.send_show_command("sh clock"))
        print(r1.send_show_command("sh ip int br"))
        print(r1.send_show_command("sh run | i hostname"))
