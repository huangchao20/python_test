class Wapen:
    def prick(self, heat):
        heat -= 500
        print(heat)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.wapen = Wapen()

p1 = Person("日泰","78")
heat = 1000
p1.wapen.prick(heat)
