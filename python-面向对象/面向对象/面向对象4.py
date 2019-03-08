#coding=utf-8

import time
class TestClass:
    name = '赵四儿'
    __gender = 'lv'
    def __init__(self, age, hobby, test, foo):
        self.age = age
        self.hobby = hobby
        self.__test = test
        self.foo = foo

    @classmethod
    def func1(cls):
        print('cls  Name:', cls.name)
        print('[---------------func1---------------]')

    def func2(self):
        print("[***************func2[%s]**************]" % TestClass.__gender)
        print('[***************func2[%s]**************]' % self.__test)
        st = time.time()
        t = self.foo
        print(t())
        print('总共耗时:[%s]' % (time.time() - st))


    @staticmethod
    def func3():
        print('[^^^^^^^^^^^^^^^func3^^^^^^^^^^^^^^^^]')

    def __printinfo(self):
        print(TestClass.name)
        print(TestClass.__gender)
        print(self.age)
        print(self.hobby)

    def printfunc(self):
        self.__printinfo()

class TestClass2(TestClass):
    def __init__(self):
        super(TestClass, self).__init__()
    def foo2(self):
        print('-----------------[%s]' % TestClass2.name)

def  func4():
    su = 1
    print('开始运行func4')
    for i in range(1, 50000):
        su *= i
    return su

if __name__ == '__main__':
    t = TestClass(18, "nv", 'testfunc', func4)
    t.func1()
    t.func2()
    t.func3()
    print('-----------------------------------------')
    print(t.name)
    print('-----------------------------------------')
    t.printfunc()
    print('-----------------------------------------')
    # print(t.__test) 不能这样访问私有变量

    # print(t.__gender)

    t2 = TestClass2()
    t2.foo2()