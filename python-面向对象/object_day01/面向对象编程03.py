
# class MyClass:
#     @classmethod
#     def foo(self):
#         print(id(self), 'foo')
# if __name__ == '__main__':
#     a = MyClass()
#     a.foo()
#     print(id(a))

class A:
    a = '赵二娃'
    def __init__(self):
        print("this can be Printed by B??")

    def fatherMethed(self):
        print("this come from A")

class B(A):
    # def __init__(self):
    #     print("xiaobizaizi")

    def sonMethed(self):
        print('suibianla')

    def fatherMethed(self):
        print("zhelishixiaobizaizi")


class Test1:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def eat(self):
        print('%s:打算将大家肯定' %self.name )

    @staticmethod
    def speak(name):
        print("%s爱说脏话" %name)



class Test2:
    name = '123'
    def __init__(self, name):
        self.name = name

    @classmethod
    def eat(self):
        print('%s爱吃鱼' %Test2.name)

class Test3:
    def __init__(self, name):
        self.name = name

    @property
    def eat(self):
        print("%s正在胡吃海塞" %self.name)

if __name__ == '__main__':
    # b = B()
    # # b.sonMethed()
    # b.fatherMethed()
    # t = Test1('铁蛋')
    # t.eat(t)
    # t.speak('赵二牛')
    t2 = A()
    print(t2.a)
    print(t2.fatherMethed)
