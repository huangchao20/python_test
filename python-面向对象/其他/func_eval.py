#coding=utf-8
x = 10
def func():
    y = 20
    t = '---------------'
    a = eval('x + y')
    print('a--------------->', a)
    b = eval('x + y', {'x':1, 'y':2})
    print('b--------------->', b)
    c = eval('x + y', {'x': 2, 'y': 3}, {'m': 11, 'v': 1})
    print('c--------------->', c)
    print('-----------------------------------------------------')
    d = eval('print(x, t, y)')
    print('d--------------->', d)


y = 20
exet = """
z = 11
s =x + y + z
print(s)
"""


def func1():
    t = '---------------'
    exec(exet)
    exec(exet, {'x': 1, 'y': 2})
    exec(exet, {'x': 2, 'y': 3}, {'x': 1,'m': 11, 'v': 1, 'z': 15})
    print('-----------------------------------------------------')
    exec('print(x, t, y)')


class Persion(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __new__(cls, name, age):
        if 0 < age < 150:
            return object.__new__(cls)
        else:
            return None
    def __str__(self):
        return '{0}{1}'.format(self.__class__.__name__, self.__dict__)

# func()
# func1()

# p1 = Persion('赵日天', 18)
# print(p1)
# # print(p1['name'])
# # print(p1['age'])
# print(Persion('赵阿妹', 201))

str = 'globle'
def func2():
    # global str
    str = 'local'
    print(str)

if __name__ == '__main__':
    func2()
    print(str)

from openpyxl import load_workbook