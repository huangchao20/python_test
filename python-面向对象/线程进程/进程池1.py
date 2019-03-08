from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
import time
import random
import os
def foo1(n):
    print('getid', os.getpid())
    time.sleep(random.randint(1, 3))
    return n ** 2

if __name__ == '__main__':
    t = ProcessPoolExecutor(max_workers=5)
    fs = []
    for i in range(100):
        f = t.submit(foo1, i)
        fs.append(f)
    t.shutdown(True)
    for f in fs:
        print(f.result())
