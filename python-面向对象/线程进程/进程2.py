import  multiprocessing as mp
import  time
import os

def foo2(q):
    for i in range(20):
        q.put('p_name:%s-----python--%s'%(__name__, i))
        time.sleep(1)

if __name__ == '__main__':
    mp.get_context('spawn')
    q = mp.Queue()
    q1 = mp.Process(target=foo2, args=(q,))
    q2 = mp.Process(target=foo2, args=(q,))
    q1.start()
    q2.start()
    for i in range(100):
        print(q.get())
    # q1.join()
    # q2.join()
