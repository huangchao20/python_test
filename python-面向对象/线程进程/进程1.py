from multiprocessing import Process
import multiprocessing
import os

def info(title):
    print('title')
    print('model name', __name__)
    print('fpid:', os.getppid())
    print('spid:', os.getpid())

def f(name):
    info('function f')
    print('hello', name)

def foo(q):
    q.put('123')
    q.put('abc')
    q.put('xx')

if __name__ == '__main__':
    # info('mian process')
    # p = Process(target=f, args=('Bob',))
    # p.start()
    # p.join()
    multiprocessing.set_start_method('spawn')
    mp = multiprocessing.Queue()
    f = Process(target=foo, args=(mp,))
    f.start()
    print(mp.get())
    print(mp.qsize())
    print(mp.get())
    print(mp.qsize())
    print(mp.get())
    f.join()

