#encoding=utf-8
class Fa:
    def __init__(self):
        self.__func()

    def __func(self):
        print('1111111111111111111111111111111111111111111111111111111')
        print('f 的 func')

class Son(Fa):
    def __init__(self):
        self.__func()
    def __func(self):
        print('son的func')


    def _Fa_func(self):
        print('Son F Func')

class Foo:
    def __foo(self):
        print('from foo')
class Bar(Foo):
    _a = 123
    def __func(self):
        print('from bar')

if __name__ == '__main__':
    # s = Son()
    # print(Fa.__dict__)
    b = Bar()
    print('MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM')
    print(b)
    print('WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW')
    b._Foo__foo()
    b._Bar__func()
