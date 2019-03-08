import time
from threading import Thread

def foo1( data ):
    for i in range(5):
        print('foo1:', i)
        time.sleep(data)

def foo2( data ):
    for i in range(10):
        print('foo2', i)
        time.sleep(data)

class Traversal:
    def __init__(self, data, name):
        self.data = data
        self.name = name
        self._rungevent(self.data, self.name)

    def _rungevent(self, data, name):
        for i in range(5):
            print("process name:", name, '\tindex', i )
            time.sleep(data)

if __name__ == '__main__':
    t1 = time.time()
    print('开始时间:', t1)
    tasks = [foo1, foo2]

    threads = []
    for task in tasks:
        t = Thread( target=task, args=(1,))
        threads.append(t)
    for t in threads:
        t.setDaemon(True)
        t.start()
    for i in threads:
        i.join()
    print('end time:', (time.time() - t1))
