import threading
import time

class MyThread(threading.Thread):
    def run(self):
        tot.acquire()
        print('this is start' ,self.getName())
        time.sleep(2)
        tot.release()


if __name__ == '__main__':
    tot = threading.BoundedSemaphore(4)

    for i in range(30):
        t1 = MyThread()
        t1.start()
    t1.join()
    print("[--------------end----------------]")
