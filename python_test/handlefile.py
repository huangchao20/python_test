import os

def fetch( filename , yfeatch ):
	print("开始查询。。。")
	search = " ".join( ("backend" ,yfetch[0]["backend"]) )	#拼接查询开始语句'backend www.oldboy20.org'
	t = "%s server %s %s weigth %s maxconn %s " %(" "*8, s["record"]["server"], s["record"]["server"], s["record"]["weight"], s["record"]["maxconn"] )#目标语句：'         server 2.2.2.3 2.2.2.3 weigth 20 maxconn 3000 '
	if not os.path.isfile( filename ):
		print("【%s】不是文件，请确认" %filename )
		return None
	with open( filename, "r+" ) as ffetch:
		for t_read in ffetch:
			if t_read == search:
				continue
	

def addf( ):
	pass
	
def deletef():
	pass

def modify():
	pass

choice = {
	"1": fetch,
	"2": addf,
	"3": deletef,
	"4": modify,
	"5": exit
}	

if __name__ == "__main__":
	filename = "F:\\黄小宝的宝\\python_test\\python_test\\haproxy.conf"
	print( choice )
	while True:
		ychoice = input( "请输入你要执行的操作： " )
		yfetch = input( "请输入您想要查询的内容： " )
		choice[ ychoice ]( filename, yfetch  )

#[{'backend':'www.oldboy20.org','record':{'server':'2.2.2.3','weight':20,'maxconn':3000}},{'backend':'www.oldboy10.org','record':{'server':'10.10.0.10','weight':9999,'maxconn':33333333333}}]