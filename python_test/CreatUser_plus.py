filename = "F:\\黄小宝的宝\\python_test\\python_test\\user.txt"
state_dict ={ "username":None, "login":False }
def Createuser():
	print("欢迎注册用户信息，有惊喜哟~~")
	username = input( "用户名:" )
	passwd = input( "密码:"  )
	with open( filename, "r+" ) as f:
		for l in f:
			if username == l.split(" ")[0]:
				print( "您注册的用户【%s】已经注册！不能重复注册" %username )
				return None
		user = " ".join((username, passwd) )
		f.read()
		f.write("\r\n")
		f.write( user )
		print( "恭喜您【%s】,您已注册成功!" %username[0] )
		return filename

def outside( type1 = "filedb" ):	
	def checkuser( func ):
		def checker( *args, **kwargs ):
			if type1 == "filedb":
				s = []
				if state_dict["username"] and state_dict[ "login" ]:
					res = func( *args, **kwargs )
					return res
				username = input( "XX用户名XX:" )
				passwd = input( "密码:" )
				
				flag = False
				with open( filename ) as f:
					for t in f:
						print("tTTTTTTTTTTTTTTTTTTTTTTTTT:", t)
						uname,pswd = t.split( " ")
						if username == uname and passwd == (pswd if "\n" not in pswd else pswd.split("\n")[0]):
							flag = True
							res = func( *args, **kwargs )
							state_dict["username"] = username
							state_dict["login"] = True
							return res
						elif username == t.split(" ")[0]:
							Flag = True
							print( "您输入的密码有误，请确认!!" )				
							return None
							
					if flag == False:
						answer = input( "是否注册Yy:" )
						if answer == "Y" or answer == "y":
							ret = Createuser()
							state_dict["username"] = username
							state_dict["login"] = True
							return ret
			elif type1 == "oracle":
				print("你大爷的oracle!!")
				res = func( *args, **kwargs )
				return res
			else:
				print( "你大爷才会陪你玩！" )
				res = func( *args, **kwargs )
				return res
		return checker
	return checkuser

@outside( "filedb" )
def getbak( name ):
	print("dear [%s] welcome back home!!" %name )

@outside( "oracle" )
def faver( list1 ):
	for i in list1:
		print( "最爱[%s]" %i )

@outside( "Mysql" )		
def speak( name ):
	print( "[%s] 最爱说的一句" %name)

if __name__ == "__main__":
	getbak( "赵小甜" )
	list1 = ["篮球", "足球", "小姐姐", "娃娃"]
	name = "赵日天"
	getbak( name )
	print("OVER?")
	faver( list1 )
	print("11")
	speak( name )
