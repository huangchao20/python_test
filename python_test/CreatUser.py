userlist = [
	["huangdabao", "cs123456" ],
	["litiedan","123"],
	["zhaotieniu", "123789" ]
]
state_dict = { "username":None, "login": False }

def Createuser():
	t = []
	username = input( "用户名:" )
	passwd = input( "密码:"  )
	t.append( username )
	t.append( passwd )
	print( t )
	for l in userlist:
		if t in userlist or t[0] == l[0]:
			print( userlist )
			print( "您注册的用户【%s】已经注册！" %t[0] )
			return None
		else:
			userlist.append( t )
			print( userlist )
			print( "恭喜您【%s】,您已注册成功!" %t[0] )
			return userlist
	
def checkuser( func ):
	def checker( *args, **kwargs ):
		s = []
		if state_dict["username"] and state_dict[ "login" ]:
			res = func( *args, **kwargs )
			return res
		username = input( "XX用户名XX:" )
		passwd = input( "密码:" )
		s.append( username )
		s.append( passwd )
		for t in userlist:
			if s == t:
				res = func( *args, **kwargs )
				state_dict["username"] = username
				state_dict["login"] = True
				return res
			elif username in t:
				print( "您输入的密码有误，请确认!!" )				
				return None
			elif username not in t:
				answer = input( "是否注册Yy:" )
				if answer == "Y" or answer == "y":
					ret = Createuser()
					print("*" * 130 )
					print( ret )
					state_dict["username"] = username
					state_dict["login"] = True
					return ret
	return checker

@checkuser
def home( name ):
	print("%s,欢迎来到恶魔的世界！！" %name )

@checkuser
def role( occupation ):		#角色
	print("亲爱的[%s]勇士，今天撸了吗？" %occupation )

@checkuser
def likes( list ):	#收藏
	for i in list:
		print( "收藏有【%s】" %( i ) )

if __name__ == "__main__":
	home( "litiedan" )
	role( "法师" )
	likelist = ["篮球", "足球", "小姐姐", "娃娃" ]
	likes( likelist )
	
