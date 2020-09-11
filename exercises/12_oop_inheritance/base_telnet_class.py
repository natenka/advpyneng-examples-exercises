import time
import telnetlib


class TelnetBase:
    def __init__(self, ip, username, password, encoding="ascii"):
        self.ip = ip
        self.encoding = encoding
        self.prompt = None

        self._telnet = telnetlib.Telnet(ip)
        self._read_until_regex("Username:")
        self._write_line(username)
        self._read_until_regex("Password:")
        self._write_line(password)
        if not self.prompt:
            time.sleep(1)
            self._telnet.read_very_eager()
        else:
            self._read_until_regex(self.prompt)

    def __str__(self):
        return f"Telnet connection to {self.ip}"

    def __repr__(self):
        return f"TelnetBase ip='{self.ip}'"

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self._telnet.close()

    def close(self):
        self._telnet.close()

    def _write_line(self, line):
        """
        Принимает как аргумент строку и отправляет на
        оборудование строку преобразованную в байты
        и добавляет перевод строки в конце.
        """
        self._telnet.write(line.encode(self.encoding) + b"\n")

    def _read_until_regex(self, regex, timeout=30):
        """
        Метод читает вывод до совпадения с регулярным выражением regex,
        если совпадения не было найдено за timeout, возвращается вывод
        считанный на данный момент.
        """
        regex_idx, match, output = self._telnet.expect(
            [regex.encode(self.encoding)], timeout=timeout
        )
        return output.decode(self.encoding)
