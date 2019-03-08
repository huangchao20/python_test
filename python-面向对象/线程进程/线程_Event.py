import threading

def do(event):
    print('this print first')
    event.wait()
    print('this ********')

event_obj = threading.Event()

# if __name__ == '__main__':
for i in range(20):
    t = threading.Thread(target=do, args=(event_obj,))
    t.start()

event_obj.clear()
inp = input('请输入:')
print(inp)
if inp == 'True':
    event_obj.set()