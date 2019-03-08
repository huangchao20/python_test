import time
from threading import Thread
def show(aggs):
    time.sleep(1)
    print(str(aggs))

if __name__ == '__main__':
    for i in range(10):
        t = Thread(target=show, args=(i,))
        t.setName("root" + str(i))
        t.start()
        t.join()
        print(t.getName())
    print('Stop')

    m = Thread( target=show, args=[])
    m.setDaemon(True)
    m.start()
    print('This is MMMMMMM')