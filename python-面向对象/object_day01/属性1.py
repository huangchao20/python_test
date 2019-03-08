#coding=utf-8
class Demo:
    name = "赵二"
    age = 18
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print(self.name)
        print(self.age)

    def get_info(self):
        print('func get_info')
        print('name:', self.name)
        print('age', self.age)
        print('MMMMMMMMMMMMMMMMMMMMMMMMMMM')
        print(Demo.name)
        print(Demo.age)
        print('WWWWWWWWWWWWWWWWWWWWWWWWWWW')

    def set_info(self, nam, ag):
        self.age = ag
        self.name = nam

if __name__ == '__main__':
    t = Demo('日天', 22)
    t.get_info()

    print(t.name)
    print(t.age)
    print('-------------------------------------')
    t.age = 28
    t.name = '赵小二'
    print('t.name')
    print(t.age)
    print('------------------------------------')
    t.get_info()