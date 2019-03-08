"""
函数可以像普通变量一样，做为函数的参数或返回值进行传递。
函数内部可以定义另外一个函数，这样做的目的可以隐藏函数功能的实现。
闭包实际也是一种函数定义形式。
闭包定义规则是在外部函数中定义一个内部函数，内部函数使用外部函数的变量，并返回内部函数的引用。
装饰器的作用是在不改变现有函数基础上，为函数增加功能。
通过在已有函数前，通过@闭包函数名的形式来给已有函数添加装饰器。
一个装饰器可以为多个函数提供装饰功能，只需要在被装饰的函数前加 @xxx 即可。
通过类也可以实现装饰器效果，需要重写 init 和 call 函数。
类实现的装饰器在装饰函数后，原来的函数引用不在是函数，而是装饰类的对象。
一个函数也可以被多个装饰器所装饰。
---------------------
作者：月夜寻花香丶
来源：CSDN
原文：https://blog.csdn.net/weixin_42943975/article/details/83960752
版权声明：本文为博主原创文章，转载请附上博文链接！
"""

import time

def time_count(func):
    def wapper():
        print('this is time_count')
        start = time.time()
        func()
        end = time.time()
        print('time_count End!!')
        print('程序总共运行时间:%s' %(end - start))
    return wapper

def time_count2(func):
    def wapper():
        print('this is time_count2')
        func()
        print("this is time_count2 End!!")
    return wapper
@time_count
@time_count2
def my_count():
    s = 0
    for i in range(0, 100000001):
        s += i
    print(s)


def my_count1():
    s = 0
    start = time.time()
    for i in range(1, 100000001):
        s += i
    end = time.time()
    print("总共耗时:%s" % (end - start))

if __name__ == '__main__':
    my_count()
    my_count1()