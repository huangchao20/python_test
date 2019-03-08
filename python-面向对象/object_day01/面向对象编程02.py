class Student:
    def __init__(self, name, age ):
        self.name = name
        self.age = age
    def tell(self):
        print("当前对象的id是:%s-------------%s" %(self.name, self.age))

    def smile(self):
        print('%s笑起来像鬼' %self.name)

class peple(Student):
    def tell(self):
        print("呵呵")


class Student1:
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


class Vector:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return 'Vector(%d, %d)' %(self.a, self.b)

    def __add__(self, other):
        return Vector(self.a + other.a, self.b + other.b)

class JustCounter:
    __a = 0
    b = 0

    def count(self):
        self.__a += 1
        self.b += 1
        print('内部访问私有变量:',self.__a)

if __name__ == '__main__':
    # student1 = Student()
    # print(student1)
    # student2 = Student()
    # print(student2)
    # p = peple("找泰迪",25)
    # p.tell()
    # p.smile()

    # student = Student1("Alex")
    # student._Student1__name = '赵四儿'
    # print(student.name)
    # v1 = Vector(5, 20)
    # v2 = Vector(2, -10)
    # print(v1 + v2)

    c = JustCounter()
    c.count()
    c.count()
    print("***************************************************")
    print(c.b)
    # print(c.__a)