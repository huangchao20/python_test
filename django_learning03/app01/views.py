from django.shortcuts import render
from app01 import models
# Create your views here.

def students(request):
    # print("[-------------------------------------]")
    # ret = request.method
    # print(ret)
    # print(request)
    # print("[************************************]")
    stu_list = models.Student.objects.all()
    return render(request, 'student.html', {'stu_list': stu_list})

def add_student(request):
    pass

def del_student(request):
    pass

def get_pagenum(p):
    USER_LIST = []
    perpage = 50
    for i in range(1, 999):
        temp = {'name':'root' + str(i), 'age': i}
        USER_LIST.append(temp)
    totalnum = len(USER_LIST)
    d = totalnum/perpage
    if type(d) != int:
        totalpage = d + 1
    else:
        totalpage = d

    if p.isdigit() and (p < 0 or p > totalpage):
        print("输入页数不存在")
    elif p.isdigit():
        pass
    else:
        print("请输入数字")

    return 0




def index(request):
    data = get_pagenum(request.GET.get('p'))
    return render(request, 'index.html', {'user_list': data})