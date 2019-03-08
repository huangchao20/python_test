import requests
from bs4 import BeautifulSoup

from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Encountered a start tag:", tag)

    def handle_endtag(self, tag):
        print("Encountered an end tag :", tag)

    def handle_data(self, data):
        print("Encountered some data  :", data)

parser = MyHTMLParser()

iurl = 'http://news.sina.com.cn/c/nd/2017-08-03/doc-ifyitapp0128744.shtml'
#iurl = 'https://www.taobao.com/'
res = requests.get(iurl)
 
res.encoding = 'utf-8'
 
#print(len(res.text))
 
soup = BeautifulSoup(res.text,'html.parser')
print(soup)
"""
print("******************************************************************")
parser = MyHTMLParser()
parser.feed(str(soup))
print("******************************************************************")
"""
#标题
H1 = soup.select('#artibodyTitle')[0].text
print("******************************************************************")
print(H1)
print("******************************************************************")
#来源
time_source = soup.select('.time-source')[0].text
print("******************************************************************")
print(time_source)
print("******************************************************************")
 
#来源
origin = soup.select('#artibody p')[0].text.strip()
print("******************************************************************")
print(origin)
print("******************************************************************")
#原标题
oriTitle = soup.select('#artibody p')[1].text.strip()
print("******************************************************************")
print(oriTitle)
print("******************************************************************")
#内容
raw_content = soup.select('#artibody p')[2:19]
content = []
for paragraph in raw_content:
    content.append(paragraph.text.strip())
'@'.join(content)    
#责任编辑
print( 10  * "*")
print(soup.select('.article-editor')[0])
ae = soup.select('.article-editor')[0].text
print("******************************************************************")
print(ae)
print("******************************************************************")
