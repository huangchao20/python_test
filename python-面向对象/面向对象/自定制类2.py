#encoding=utf-8

class Fin:
    def __init__(self):
        self.a = 0
        self.b = 1

    def __iter__(self):
        return  self

    # def __next__(self):
    #     self.a, self.b = self.b, self.a + self.b
    #     if self.a > 100000000000:
    #         return StopIteration()
    #     return self.a

    def __getitem__(self, n):
        for i in n:
            self.a, self.b = self.b, self.a + self.b
            if self.a > 100000000000:
                return StopIteration()
            return self.a
if __name__ == '__main__':
    f = Fin()
    print(f[1])