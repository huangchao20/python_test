#coding=utf-8

class Socre:

    @property
    def score(self):
        print('1111111')
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('输入的不是整数！！！')
        elif value < 0 or value > 100:
            raise ValueError('成绩只能是0 ~ 100！！')
        print(22222222)
        self.__score = value

if __name__ == '__main__':
    s = Socre()
    s.score = 100
    t = s.score
    print(t)
