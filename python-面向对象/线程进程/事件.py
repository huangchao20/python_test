import threading
def show(e):
    print('start')
    e.wait()
    print('Done')

if __name__ == '__main__':
    e = threading.Event()
    for i in range(10):
        t = threading.Thread(target=show, args=(e,))
        t.start()

        isInput = input('>>>>>')
        if isInput == '1':
            e.set()
        e.clear()