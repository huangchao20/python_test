#coding=utf-8
from test import TestClass

def func():
    tt = TestClass('小伙子', 98)
    print('------------------------------')
    print(tt.__doc__)
    print('------------------------------')
    print(tt.__module__)
    print('------------------------------')
    print(tt.__class__)
if __name__ == '__main__':

    tt = func()