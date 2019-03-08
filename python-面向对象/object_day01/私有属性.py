#coding=utf-8
class Person:
    def __init__(self, weight, height, name, sex):
        self.__weight = weight
        self.__name = name
        self.__height = height
        self.sex = sex

    def tell_bmi(self):
        return self.__weight/self.__height **2

    def tell_hei(self):
        print(self.__height)

    def tell_wei(self):
        print(self.__weight)

    def set_wei(self, wei):
        if wei >= 20:
            self._weight = wei
        else:
            print('你TMD瘦成猴了')

if __name__ == '__main__':
    t = Person(83, 1.73, 'aidahuang', 'meal')
    print(t.tell_bmi())
    t.set_wei(70)
    print(t.tell_bmi())