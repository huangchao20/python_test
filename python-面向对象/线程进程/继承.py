import threading
import time

class MyThread(threading.Thread):
    def __init__(self):
        super(MyThread, self).__init__()
        self.name = self.name.split('-')[1]
        # print(self.name)

    def run(self):
        super(MyThread, self).run()
        print('start on threading', self.name)
        time.sleep(5)
        print('你好毒：', self.name)

if __name__ == '__main__':
    print('开启主线程')
    ttr = []
    for i in range(10):
        t = MyThread()
        ttr.append(t)
    for t in ttr:
        t.setDaemon(True)
        t.start()
        t.setName('呵呵你一脸--{}'.format(i))
        print('启动线程', t.getName())
    for t in ttr:
        t.join()

    print('------------end-------------')