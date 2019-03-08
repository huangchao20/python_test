class BirthDay:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


class Couse:
    def __init__(self, name, price, period):
        self.name = name
        self.price = price
        self.period = period

class Teacher:
    def __init__(self, name, gender, birth, couse):
        self.name = name
        self.gender = gender
        self.birth = birth
        self.couse = couse

    def teach(self):
        print("%s:正在上%s课")

teacher = Teacher(
    "赵日天", "公",
    BirthDay("1990","05","23"),
    Couse("pyhton", "58.1", "3 weeks")

)

