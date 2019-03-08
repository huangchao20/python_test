#coding=utf-8
class Teacher():
    def __init__(self, name, level):
        self.name = name
        self.__level = level

    def get_name(self):
        return self.name

    def get_level(self):
        return  self.__level

# def get_name()
if __name__ == '__main__':
    t = Teacher('赵二','33')
    print('老师叫什么：%s' % t.get_name())
    print('老师多少级: %s' % t.get_level())