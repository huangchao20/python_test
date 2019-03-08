import queue

lifoqueue = queue.LifoQueue()

lifoqueue.put('1')
lifoqueue.put('2')
lifoqueue.put('3')
print(lifoqueue.qsize())
print(lifoqueue)
print(lifoqueue.get())
print(lifoqueue.get())
print(lifoqueue.get())

fifoqueue = queue.PriorityQueue()
fifoqueue.put(4)
fifoqueue.put(5)
fifoqueue.put(6)
print(fifoqueue.get())
print(fifoqueue.get())
print(fifoqueue.get())
