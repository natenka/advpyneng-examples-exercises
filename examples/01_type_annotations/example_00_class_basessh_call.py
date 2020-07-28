from example_00_class_basessh import BaseSSH

if __name__ == "__main__":
    r1 = BaseSSH("192.168.100.1", "cisco", "cisco")
    print(r1.send_show_command("sh ip int br"))
    print(r1.send_show_command("enable"))
    print(r1.send_show_command("cisco"))
    print(
        r1.send_config_commands(
            ("conf t", "int loopback 33", "ip address 3.3.3.3 255.255.255.255", "end")
        )
    )
