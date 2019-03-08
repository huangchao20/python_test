import requests
import os
from bs4 import BeautifulSoup

def requests_get( URL ):
    print( URL )
    filepath = "F:\\黄小宝的宝\\python_test\\spider"
    filename = "blog_HTML.html"
    os.chdir( filepath )
    with open( filename, "r+", encoding = "utf8" )as f:
        print("11111那里报错拉？？？")
        res = requests.get( URL )
        print(res)
        #res = BeautifulSoup(requests.get( URL ))
        print("22222那里报错拉？？？")
        #doct = BeautifulSoup(res)
        print("33333那里报错拉？？？")
        f.write( res.text )
    return res

if __name__ == "__main__":
    URL = "https://blog.csdn.net/nzjdsds/article/details/77506254"

    res = requests_get( URL )
    print(res )
