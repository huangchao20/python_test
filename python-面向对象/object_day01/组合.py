#coding=gbk
import time
from abc import ABCMeta, abstractclassmethod, abstractmethod
class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_info(self):
        print('传入的参数a:[%s]' % self.a)
        print('传入的参数b:[%s]' % self.b)

    def foo(self):
        print('type测试打印')
        print(type(self.a))
        print(type(self.b))

        if (isinstance(self.a, int) or isinstance(self.a, float)) and(isinstance(self.b, int) or isinstance(self.b, float)):
            return self.a * self.b
        elif isinstance(self.a, str) and isinstance(self.b, int):
            ret = '[%s]是字符串，[%d]是整形' % (self.a, self.b)
            return ret
        elif isinstance(self.a, str) and isinstance(self.b, str):
            ret = '[%s],[%s]都是字符串' % (self.a, self.b)
            return ret
        else:
            ret = '不知道是什么鬼'
            return ret

class B:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def foo2(self):
        s = A(self.a, self.b)
        print(s.print_info())
        print(s.foo())

class C:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.A = A(self.a, self.b)

    def fooC(self):
        self.A.print_info()

        if isinstance(self.A.foo(), int):
            return 'OK'
        else:
            return 'NOT OK'
class E:
    @abstractmethod
    def tool(self):
        pass
    
class D(E):
    def fooD(self):
        inp1 = input('>>>>inp1:')
        inp2 = input('>>>>inp2:')

        day = time.ctime()
        res = A(inp1, inp2)
        return day, res

class E(D):
    pass

class F(metaclass=ABCMeta):
    @abstractclassmethod
    def func1(self):
        pass
class Alipay:
    def pay(self):
        print('123')


if __name__ == '__main__':
    # t = B('huangchao', 12)
    # t.foo2()

    # t2 = C(1, 2)
    # print(t2.fooC())

    t3 = D()
    c, d = t3.fooD()
    print(c)
    print(d.foo())
    print(E.__base__)
