#encoding=gbk
from abc import ABCMeta, abstractmethod,abstractclassmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def eat(self):
        print('打开粮食袋子')
        print('放一个碗')
        print('将粮食倒进碗里')

    @abstractmethod
    def sleep(self):
        pass

class Dog(Animal):
    def eat(self):
        super().eat()
        print('狗再吃食')
    def sleep(self):
        print('------------------------')
        print('你在睡觉')

if __name__ == '__main__':
    t = Dog()
    t.eat()
    t.sleep()


