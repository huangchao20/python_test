import threading

def condition_func():
    ret = False
    ipt = input('>>>>:')
    if ipt == '1':
        ret = True
    return ret

def run(n):
    con.acquire()
    con.wait_for(condition_func)
    print('run for ', n)
    con.release()
    print('------------------------')

if __name__ == '__main__':
    con = threading.Condition()
    for i in range(20):
        t = threading.Thread(target=run, args=(i,))
        t.start()
        t.join()
    print('I am ok')

