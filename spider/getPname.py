import os
import xlrd

def getPnames( ppath ):
	listp = ["PyTrade_fbap", "PyComponent_fbap", "component_fbap", "PyTrade_ABOP"]
	PyTrade_fbap  = []
	PyComponent_fbap = []
	component_fbap = []
	PyTrade_ABOP = []
	listlist = []
	listlist = [PyTrade_fbap, PyComponent_fbap, component_fbap, PyTrade_ABOP]
	pathlist = os.listdir( ppath )
	for t in pathlist:
		listlst[listp.index(t)] = os.lisdtdir( os.path.join( ppath, t ))
		
	
if __name__ == "__main__":
	ppath = "E:\\SVN\\20180726\\workspace"
	