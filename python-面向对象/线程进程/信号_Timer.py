import threading
import time

def run():
    rlock.acquire()
    print('123')
    time.sleep(1)
    rlock.release()

if __name__ == '__main__':
    rlock = threading.RLock()
    for i in range(20):
        t = threading.Timer(5.0, run)
        t.start()
    t.join()
    print('Over')