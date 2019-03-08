import queue

def show(q, n):
    if q.empty() or q.qsize() >= 1:
        print('*******%s*******' %q.qsize())
        q.put(n)
    else:
        print('queue not size')

if __name__ == '__main__':
    q = queue.Queue(5)
    for i in range(5):
        show(q, i)
    print('queue is number:', q.qsize())
    for i in range(5):
        print(q.get())
    print('------------end------------')