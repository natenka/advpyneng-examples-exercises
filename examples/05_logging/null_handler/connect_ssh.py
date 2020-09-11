from base_ssh_class import BaseSSH
import logging

logging.basicConfig(level=logging.DEBUG)

r1 = BaseSSH("192.168.100.1", "cisco", "cisco")

print(r1.send_show_command("sh clock"))

r1.close()
