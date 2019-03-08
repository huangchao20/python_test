from urllib import request
from bs4 import BeautifulSoup

f1 = open( "NoSoup.txt", "w", encoding = "utf8 ") 
f2 = open( "WhitSoup.txt", "w", encoding = "utf8 ")

url = r'http://www.jianshu.com'
# 模拟真实浏览器进行访问
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
page = request.Request(url, headers=headers)
page_info = request.urlopen(page).read()
page_info = page_info.decode('utf-8')
f1.write(str(page_info ))

# 将获取到的内容转换成BeautifulSoup格式，并将html.parser作为解析器
soup = BeautifulSoup(page_info, 'html.parser')
f2.write(str(soup ))
f1.close()
f2.close()

# 以格式化的形式打印html
# print(soup.prettify())
titles = soup.find_all('a', 'title')  # 查找所有a标签中class='title'的语句
# 打印查找到的每一个a标签的string

