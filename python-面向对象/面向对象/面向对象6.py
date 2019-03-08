#coding=utf-8

class Student():
    count = 0
    print('Student:', count)
    def __init__(self, name):
        self.name = name
        self.print_Info()

    def print_Info(self):
        print(self.name)
    # def countPlus(self):
    #     Student.count += 1
    #     print(1111111111111111111111)
        Student.count += 1

if __name__ == '__main__':
    s1 = Student('11')
    s2 = Student('22')
    s3 = Student('33')
    s4 = Student('44')
    s5 = Student('55')
    s6 = Student('66')
    print(Student.count)
