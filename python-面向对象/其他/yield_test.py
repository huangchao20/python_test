
user_list = [
    {"id": 222, "name": "haiyan", "age": 33},
    {"id": 1, "name": "xxx", "age": 18},
]

class Foo(object):
    def __init__(self, args):
        self.args = args

    def __iter__(self):
        for item in self.args:
            yield item
            yield {'age':item['age'] + item['id']}

def main():
    obj = Foo(user_list)
    for i in obj:
        print('[******************************%s]' %i)

if __name__ == '__main__':
    main()