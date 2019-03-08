a = 1
def foo():
    print(123)
    global a
    a += 3
    print(a)

foo()
print(a, end='\r\n')