#coding=utf-8

class Student:
    __slots__ = ('name', 'age')
    

if __name__ == '__main__':
    s = Student()
    s.name = "赵不二"
    s.age = 18
    # s.gender = "F"

    print(s.name)
    print(s.age)
    # print(s.__dict__)
    s2 = Student()
    # print(s2.__dict__)