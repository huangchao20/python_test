import os

import time

def foo():
    while True:
        print(time.ctime())
        time.sleep(1)


if __name__ == "__main__":
    foo()
