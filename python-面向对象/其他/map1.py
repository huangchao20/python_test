import win32com


def printwin32com_Info():
    print(dir(win32com))

def fun(x, y):
    return (x , y)

# m = [2, 3, 4, 5, 6, 7, 8, 1]
# n = [2, 3, 4, 5, 6, 7, 8, 9]
# z = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# t = list(map(fun, m, z))
# print(type(t))
# print(t)

def func():
    while True:
        inp = input(">>>>>>:")
        if inp.isdigit():
            t = int(inp)
            return t
        else:
            try:
                t = float(inp)
                return t
            except Exception as e:
                print(e)
                continue

# def func2():
#     while True:
#         inp = input('>>>>>>>>>>>>>>:')
#         print(type(inp))
#         if isinstance(eval(inp), (int, float)):
#             if inp.isdigit():
#                 print(int(inp))
#                 t = int(inp)
#             else:
#                 t = float(inp)
#             return t
#         else:
#             continue
#
# func2()

if __name__ == '__main__':
    printwin32com_Info()