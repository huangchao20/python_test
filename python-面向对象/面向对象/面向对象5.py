#coding=utf-8

class Animal():

    def run(self):
        print('Animal is running!!')

class Dog(Animal):
    def run(self):
        print('Dog is running!!')

class Cat(Animal):
    def run(self):
        print('Cat is running!!')

class Hasqy(Dog):
    def run(self):
        print('欢乐的亦凡在奔跑！！')

def run_twice(animail):
    animail.run()
    animail.run()


if __name__ == '__main__':
    d = Dog()
    c = Cat()
    a = Animal()
    吴亦凡 = Hasqy()

    run_twice(d)
    run_twice(c)
    run_twice(a)

    print("吴亦凡是狗:", isinstance(吴亦凡, Dog))
    print("吴亦凡是哈士奇:", isinstance(吴亦凡, Hasqy))
    吴亦凡.run()