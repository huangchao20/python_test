from multiprocessing import Process,Pipe

def foo(f, c):
    f.send('f_send_message1')
    f.send('f_send_message2')
    f.send('ff')
    c.send('c_send_message1')
    c.send('c_send_message2')
    c.send('c_ss')
    f.close()
    c.close()

if __name__ == '__main__':
    f, c = Pipe()
    pr = Process(target=foo, args=(f, c,))
    pr.start()
    # print('f1', f.recv())
    # print('f2', f.recv())
    print('c1', c.recv())
    print('c2', c.recv())
    print('c3', c.recv())
    print('c4', c.recv())
    pr.join()
    print('------------------end--------------------')