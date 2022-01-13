from base_ssh_class import BaseSSH
import logging

logging.getLogger("paramiko").setLevel("INFO")

logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s %(name)s %(levelname)s %(message)s"
)


logging.debug("Важный текст")
r1 = BaseSSH("192.168.100.1", "cisco", "cisco")
print(r1.send_show_command("sh clock"))
