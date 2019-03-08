#coding=utf-8
class Car:
    color = 'green'
    speed = '2m/s'
    def move(self):
        print('一辆拖拉机正飞驰在乡间的小路上')
    def toot(self):
        print('它一边开，一边哔哔的按喇叭')

if __name__ == '__main__':
    c = Car()
    c2 = Car()
    c.move()
    c.toot()
    c.color = 'yellow'
    c.speed = '200m/s'
    print(c.color)
    print(c.speed)
    print(Car.__dict__)
    print('---------------------------------')
    print(c2.speed)
    print(c2.color)