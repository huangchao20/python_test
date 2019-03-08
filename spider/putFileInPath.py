import os

def getcwdfileTT( abs ):	#传入文件列表或者路径
	listp = ["PyTrade_fbap", "PyComponent_fbap", "component_fbap", "PyTrade_ABOP"]
	PyTrade_fbap  = []
	PyComponent_fbap = []
	component_fbap = []
	PyTrade_ABOP = []
	listlist = []
	listlist = [PyTrade_fbap, PyComponent_fbap, component_fbap, PyTrade_ABOP]
	if abs == None:
		print( "请检查您输入是否为空" )
		return None
	if type(abs) is list:	#获取将xcel文件中文件名放到对应的目录下面
		for i in range( len( abs )):
			for files in abs[i]:
				ff = files.split("/")
				#print( listlist )
				listlist[ listp.index( ff[2] )].append( ff[3])
	return listlist
	
def getcwdfile( abs ):	#传入文件列表或者路径
	listp = ["PyTrade_fbap", "PyComponent_fbap", "component_fbap", "PyTrade_ABOP"]
	PyTrade_fbap  = []
	PyComponent_fbap = []
	component_fbap = []
	PyTrade_ABOP = []
	listlist = []
	listlist = [PyTrade_fbap, PyComponent_fbap, component_fbap, PyTrade_ABOP]
	if abs == None:
		print( "请检查您输入是否为空" )
		return None
	if type(abs) is list:	#获取将xcel文件中文件名放到对应的目录下面
		for i in range( len( abs )):
			for files in abs[i]:
				ff = files.split("/")
				print( listlist )
				listlist[ listp.index( ff[2] )].append( ff[3])
	else:  	#获取远程桌面获取的文件
		print("A" * 150 )
		print("V" * 150 )
		os.chdir( abs )	
		for i in range( len( listp ) ):
			pathp = os.path.join(abs, listp[i] )
			os.chdir( pathp )
			listlist[listp.index( listp[i] )] = os.listdir( os.getcwd() )
	return listlist
	
if __name__ =="__main__":
	a = [
	['./workspace/PyTrade_fbap/TBATCH_Proc_M0001.py', './workspace/PyTrade_fbap/TBATCH_Proc_M0002.py'], 
	['./workspace/PyTrade_fbap/TCHCP_C0008.py'], 
	['./workspace/PyTrade_fbap/T0816000010_D0201.py', './workspace/PyComponent_fbap/SS_0816000010.py', './workspace/PyTrade_fbap/TPU_TRANS_510000_S0102.py', './workspace/PyTrade_ABOP/TSS_SSDS_510700_D0201.py', './workspace/PyTrade_ABOP/TSS_SSDS_510700_D0202.py', './workspace/PyTrade_ABOP/TSS_SSDS_510700_D0203.py', './workspace/PyTrade_ABOP/TSS_SSDS_510700_D0204.py', './workspace/PyTrade_ABOP/TSS_SSDS_510700_D0206.py', './workspace/PyTrade_ABOP/TSS_SSDS_510700_D0207.py', './workspace/PyTrade_ABOP/TSS_SSDS_510700_D0209.py', './workspace/PyTrade_ABOP/TSS_SSDS_510700_D0212.py', './workspace/component_fbap/P_Time.py'], 
	['./workspace/PyTrade_ABOP/T0283000005_D0201.py', './workspace/PyTrade_ABOP/T0283000005_D0202.py', './workspace/PyTrade_ABOP/T0283000005_D0203.py', './workspace/PyTrade_ABOP/T0283000005_D0204.py', './workspace/PyTrade_ABOP/T0283000005_D0205.py', './workspace/PyTrade_ABOP/T0283000005_D0206.py', './workspace/PyTrade_ABOP/T0283000005_D0207.py', './workspace/PyTrade_ABOP/T0283000005_D0208.py', './workspace/PyTrade_ABOP/T0283000005_D0209.py', './workspace/PyTrade_ABOP/T0283000005_D0210.py', './workspace/PyTrade_ABOP/T0283000005_D0211.py', './workspace/PyTrade_ABOP/T0283000005_D0212.py', './workspace/PyTrade_fbap/T0283000005_P0101.py', './workspace/PyTrade_fbap/T0283000005_P0102.py'], 
	['./workspace/PyTrade_fbap/T0817000008_B0101.py', './workspace/PyTrade_fbap/T0817000008_B0102.py', './workspace/PyTrade_fbap/T0817000008_B0103.py', './workspace/PyTrade_fbap/T0817000008_B0104.py', './workspace/PyTrade_fbap/T0817000008_B0105.py', './workspace/PyTrade_fbap/T0817000008_B0106.py', './workspace/PyTrade_fbap/T0817000008_B0107.py', './workspace/PyTrade_fbap/T0817000008_B0108.py', './workspace/PyTrade_fbap/T0817000008_B0109.py', './workspace/PyTrade_fbap/T0817000008_B0111.py', './workspace/PyTrade_fbap/T0817000008_B0113.py', './workspace/PyTrade_fbap/T0817000008_B0114.py', './workspace/PyTrade_fbap/T0817000008_B0115.py', './workspace/PyTrade_fbap/T0817000008_B0117.py', './workspace/PyTrade_fbap/T0817000008_B0119.py', './workspace/PyTrade_fbap/T0817000008_D0101.py', './workspace/PyTrade_fbap/T0817000008_D0102.py', './workspace/PyTrade_fbap/T0817000008_D0103.py', './workspace/PyTrade_fbap/T0817000008_F0101.py', './workspace/PyTrade_fbap/T0817000008_F0102.py', './workspace/PyTrade_fbap/T0817000008_F0103.py', './workspace/PyTrade_fbap/T0817000008_F0104.py', './workspace/PyTrade_fbap/T0817000008_K0101.py', './workspace/PyTrade_fbap/T0817000008_K0102.py', './workspace/PyComponent_fbap/NC0817000008.py'], 
	['./workspace/PyTrade_fbap/TSHFS_0007.py', './workspace/PyTrade_fbap/TSHFS_0010.py', './workspace/PyTrade_fbap/TSHFS_0012.py', './workspace/PyTrade_fbap/TSHFS_B0001.py', './workspace/PyTrade_fbap/TSHFS_B0002.py', './workspace/PyTrade_fbap/TSHFS_B0004.py', './workspace/PyTrade_fbap/TSHFS_B0005.py', './workspace/PyTrade_fbap/TSHFS_B0006.py', './workspace/PyTrade_fbap/TSHFS_B0101.py', './workspace/PyTrade_fbap/TSHFS_D0101.py', './workspace/PyTrade_fbap/TSHFS_F0001.py', './workspace/PyTrade_fbap/TSHFS_F0002.py', './workspace/PyTrade_fbap/TSHFS_F0003.py', './workspace/PyComponent_fbap/_0283000004.py'], 
	['./workspace/PyTrade_fbap/T0000000001_B0101.py'], 
	['./workspace/PyTrade_fbap/TPHFS_D2303.py'], 
	['./workspace/PyTrade_fbap/TWPGS_OnLine_V02_S000805A119.py'], 
	['./workspace/component_fbap/B_Batch_Proc.py', './workspace/PyTrade_fbap/TBATCH_Proc_S3859.py'], 
	['./workspace/PyTrade_fbap/T0817000018_P0101.py', './workspace/PyTrade_fbap/T0817000018_P0102.py', './workspace/PyTrade_fbap/TWPGS_OnLine_V02_S000805A120.py', './workspace/PyTrade_fbap/TWPGS_OnLine_V02_S000805A121.py', './workspace/PyTrade_fbap/TWPGS_OnLine_V02_S000805A122.py', './workspace/PyComponent_fbap/OP_0817.py', './workspace/PyTrade_ABOP/T0817000018_D0201.py', './workspace/PyTrade_ABOP/T0817000018_D0202.py', './workspace/PyTrade_ABOP/T0817000018_D0203.py', './workspace/PyTrade_ABOP/T0817000018_D0204.py', './workspace/PyTrade_ABOP/T0817000018_D0205.py', './workspace/PyTrade_ABOP/T0817000018_D0206.py', './workspace/PyTrade_ABOP/T0817000018_D0207.py', './workspace/PyTrade_ABOP/T0817000018_D0208.py', './workspace/PyTrade_ABOP/T0817000018_D0209.py', './workspace/PyTrade_ABOP/T0817000018_D0210.py', './workspace/PyTrade_ABOP/T0817000018_D0211.py', './workspace/PyTrade_fbap/TWPGS_S0015.py', './workspace/PyTrade_fbap/TWPGS_Public_S001500A101.py']]
	ppath = "E:\\SVN\\20180816\\特色业务平台\\特色业务平台.20180816r.t6\\workspace"
	dpath1 = "E:\\SVN\\20180816\\特色业务平台\\特色业务平台.20180816r.t11\\workspace"
	dpath2 = "E:\\SVN\\20180816W\\特色业务平台\\特色业务平台.20180816rw.t5\\workspace"
	#llist = getpath( a )
	#print( llist )
	#print("*" * 100 )
	print( "正在处理ppath" )
	s = getcwdfile( dpath1 )
	print(s)
	print( "ppath处理完成" )
	
	print( "*" * 100 )
	print("开始处理excel文件的py文件名")
	p = getcwdfileTT( dpath2 )
	print(p)
	
