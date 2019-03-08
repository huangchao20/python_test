import threading
import time
class MyThread2(threading.Thread):
    def __init__(self, ThreadID, ThreadName):
        super(MyThread2, self).__init__()
        self.ThreadID = ThreadID
        self.ThreadName = ThreadName


    def print_time(self, suntime, threadName ):
        for i in range(3):
            Lockagein(3, 2)
            time.sleep(2)
            print('知你妹[%s],名字你妹[%s]' %(i, threadName))

    def run(self):
        threadLock.acquire()
        print('尼玛累死我了', self.ThreadName)
        self.print_time(time.time(), self.ThreadName)
        threadLock.release()

def Lockagein(avg1, avg2):
    threadLock.acquire()
    print('arithmetic:', time.time(), avg1 + avg2)
    time.sleep(2)
    threadLock.release()

if __name__ == '__main__':
    threadLock = threading.RLock()
    # threadLock = threading.Lock()    #死锁
    ttr = []
    for i in range(10):
        t = MyThread2(1, 'thread--%s' %i)
        ttr.append(t)
    for t in ttr:
        t.start()
    for t in ttr:
        t.join()
    print('啊啊啊啊啊啊啊啊啊，要死')