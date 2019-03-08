#encoding=gbk
from abc import ABCMeta, abstractmethod,abstractclassmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def eat(self):
        print('����ʳ����')
        print('��һ����')
        print('����ʳ��������')

    @abstractmethod
    def sleep(self):
        pass

class Dog(Animal):
    def eat(self):
        super().eat()
        print('���ٳ�ʳ')
    def sleep(self):
        print('------------------------')
        print('����˯��')

if __name__ == '__main__':
    t = Dog()
    t.eat()
    t.sleep()


