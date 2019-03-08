#coding=utf-8
class Test:
    c1 = '我爱你中国'
    def __init__(self, name):
        self.name = name

# obj = Test('最亲爱的母亲')
# print(obj.name)
# print(obj.c1)


class MethodClass:
    """
    【--------------
    世界之大
    无奇不有
    例如春夏与秋冬
    关我屁事
    ---------------】
    """
    __c2 = '萝卜斯基'           #私有静态字段
    c1 = '最亲爱的母亲'       #共有静态字段
    def __init__(self, name, pri):
        self.name = name
        self.pri = pri
        self.__vals = '需要重新提版'

    def putong(self):
        print('^V^俺是普通^V^')

    @classmethod
    def ClassMethod(self):
        print('老子类方法')

    @staticmethod
    def staticmeth():
        print('要你管，再看咬死你')

    comm = property(putong)
    @property
    def price(self):
        print('[%s]值[%s]分'%(self.name, self.pri))

    """
    123456
    """
    def get_bra(self):
        return 'get_bra'

    def set_bra(self, val):
        return '----------:', val

    def del_bra(self):
        print(self.__vals)
        return '123'

    TT = property(get_bra, set_bra, del_bra, '乌拉拉拉的嘘')

    def __tin(self):
        print('啦啦啦啦啦啦啦啦撸')

    def _batch(self):
        print('马上要跑批拉')


    def test(self):
        print('MMMMMMMMMMMMMMMMMMM')
        self.__tin()
        print(MethodClass.__c2)
        print('WWWWWWWWWWWWWWWWWWW')

class mt(MethodClass):
    def printinfo(self):
        print(mt.c1)
obj = MethodClass('fansi', 200)
# obj.putong()
# obj.ClassMethod()
# obj.staticmeth()
# print('--------------------------')
# obj.price
# print('VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV')

# obj.comm
obj.TT
obj.set_bra('贼辣眼睛')
# obj.TT.__dict__
del MethodClass.TT

print(obj.name)
obj.del_bra()
obj.test()

obj._batch()
print(obj.c1)
print('------------------------')
print(obj._MethodClass__c2)     #对象._类名__私有属性可访问类私有属性
print('[____________________________________________________________]')
obj._MethodClass__tin()
#obj.__tin()错误的访问方法
# print(obj.__c2)

# tt = mt('泰迪', 2000)
# tt.printinfo()


print(obj.__doc__)
print(obj.__module__)
print('-------------------')
print(obj.__class__)
