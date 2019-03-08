import time
class Date_Format:
    def __init__(self, year, mon, day):
        self.year = year
        self.mon = mon
        self.day = day

    def func1(self, flag):
        # print(self)
        # print(self.year, self.mon, self.day
        return "{0.year}{1}{0.mon}{1}{0.day}".format(self, flag)

dict_msg = {
    "1":"-",
    "2":":",
    "3":" ",
    "4":"exit",
}
message = "选择:1-->xxxx-xx-xx;2-->xxxx:xx:xx;3-->xxxx xx xx;4-->退出"
while True:
    print( message )
    t = time.localtime()
    d1 = Date_Format( t.tm_year,t.tm_mon,t.tm_mday )
    flags = (" ", "-", ":")
    flag = input("请输入日期格式:")
    print("------------------------------------>")
    print(flag)
    print((flag in dict_msg))
    print(dict_msg[flag])

    if flag in dict_msg and dict_msg[flag] == "exit":
        print("程序退出啦!!")
        break
    elif flag in dict_msg and dict_msg[flag] in flags and d1.func1(dict_msg[flag]) != None:
        print(d1.func1(dict_msg[flag]))
    else:
        print("输入不正确，请重新输入！！")