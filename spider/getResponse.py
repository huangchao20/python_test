import os
from urllib import request
def getResponse( url, file_path, filename  ):
    print(url)
    print(file_path)
    print(filename)
    os.chdir( file_path )
    print( os.getcwd() )
    response = request.urlopen( url )
    with open( filename, "w+" ) as f:
        f.write( str(response.read()) )
        response.close()

if __name__ == "__main__":
    url = "https://www.cnblogs.com/zhangmei/p/6049064.html"
    url1 = "http://www.runoob.com/python/python-100-examples.html"
    file_path = "F:\\黄小宝的宝\\python_test\\spider"
    filename = "runoob.txt"
    filename1 = "runoob1.txt"
    getResponse( url, file_path, filename )
    print("开始取100")
    getResponse( url1, file_path, filename1 )
