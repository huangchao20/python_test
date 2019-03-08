#coding=utf-8
from 字段 import MethodClass

class TestClass:
    """
    我就是我
    是不一样的你爹
    """
    __val1 = '管不着我'
    va2 = '客官不可以'
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('[%s]---------------[%s]' % (self.name, self.age))

    def foo1(self):
        print('[%s]这个龟儿子打搅到我了' % self.name )

    def foo2(self):
        print('小比崽子才[%s]' % self.age)

# def test():
#     c = MethodClass('赵不二', 199)
#     print(c.__module__)
#     print(c.__class__)

