#coding=utf-8

from 字段 import MethodClass
class Test1(MethodClass):
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('test：', self.name)
        print('^^^^^^:', self.age)

t = Test1('中华田园犬', 3)
print(Test1.__bases__)
