import time
import os


def follow(thefile):
    thefile.seek(0, os.SEEK_END)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


if __name__ == "__main__":
    log = "scrapli_example.log"
    log_lines = follow(open(log))
    for line in log_lines:
        print(line, end="")
