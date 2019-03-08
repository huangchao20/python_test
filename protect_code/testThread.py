from threading import Thread
from multiprocessing import Process

def printHello( name ):
	print( "[%s] say hello to all " %name )

if __name__ == "__main__":
	t = Thread( target = printHello , args = ("Tom",) )
	t.start()
	print( "主进程-->线程" )
	
	t1 = Process( target = printHello, args = ("Jone",) )
	t1.start()
	print( "主进程-->子进程" )
