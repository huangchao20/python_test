import re

def user_info():
    username = input("请输入用户名>>>:")
    passwd = input("请输入密码>>>:")
    telnum = input("请输入电话号码>>>:")
    email = input("请输入邮箱>>>:")

    return {
        'username': username,
        'passwd': passwd,
        'telnum': telnum,
        'email': email
    }

def authentication(user_info):
    is_vaild = True
    if len(user_info["username"]) == 0:
        print("户名不允许为空")
        is_vaild = False
    if len(user_info['passwd']) == 0:
        print("密码不允许为空")
        is_vaild = False
    if len( re.findall(r'1[0-9]{10}]', user_info['telnum'])) == 0:
        print("电话格式不正确")
        is_vaild = False

    if not re.search(r'\w+@\w+.com$', user_info['email']).group():
        print('邮箱格式不正确')
        is_vaild = False

    data = { 'is_vaild': is_vaild,
             'user_info': user_info}
    return data

class Garen:
    camp = "Demacia"
    def __init__(self, nikename, life_value , aggre_value ):
        self.nikename = nikename
        self.life_value = life_value
        self.aggre_value = aggre_value

    def attck(self, enemy):
        print(self.life_value)
        print(enemy.aggre_value)
        enemy.life_value = enemy.life_value - self.aggre_value
        print(self.life_value)

class Student():
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.count += 1

if __name__ == '__main__':
    # student1 = Student('张三', 49)
    # print(student1.__dict__)
    # print(student1.count)
    #
    # student2 = Student('赵铁钩', 19)
    # print(student2.__dict__)
    # print(student2.count)
    g = Garen('name1', 100, 200)
    r = Garen('name2', 2000, 100)
    print("name1***********%s" % g.life_value)
    print("name2***********%s" % r.life_value)
    g.attck(r)
    print('name2***********%s' %r.life_value)