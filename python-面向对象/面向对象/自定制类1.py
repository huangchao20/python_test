#encoding=utf-8

class Student:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'Student object:(name: %s)' %self.name

    # __repr__ == __str__

if __name__ == '__main__':
    s = Student('赵不二')
    s