

# 由bs4引入鸡汤
from bs4 import BeautifulSoup

# @获得beautifulsoup对象

# 声明使用lxml作为解析器，获得一碗鸡汤
# 这里必须同时装有lxml
page_text = ""
bsp = BeautifulSoup(page_text, 'lxml')

# @获得具体页面元素

# 获得 title 元素
# print(bsp.title)
# print(type(bsp.title))  # <class 'bs4.element.Tag'>

# 获得 title 元素文本
# print(bsp.title.text)
# print(bsp.title.string)

# 获得第一个div元素
# print(bsp.div)

# 获得所有div元素
# print(bsp.find_all('div'))
# print(bsp.select('div'))

# 所有拥有id属性的div元素集合列表
# print(bsp.select('div[id]'))

# 所有class属性为div_classname的所有元素
# print(bsp.select('.div_classname'))
# print(bsp.select('div[class=div_classname]'))

# 所有id属性为divid的所有元素
# print(bsp.select('#divid'))
# print(bsp.select('div[id=divid]'))

# 位置为最前面2个的div元素
# print( bsp.find_all('div', limit=2) )

# 第一个a元素的href属性
# print( bsp.a.get('href') )
# print( bsp.a.attrs['href'] )

# 第二个a元素的所有属性
# print( bsp.a.find_next('a').attrs['href'] )
# print( bsp.select('a')[1].attrs['href'] )

#id=divid的div元素一级子a元素
# print( bsp.select('div[id=divid] > a') )

#id=divid的div元素下所有层的a元素
# print( bsp.select('div[id=divid] a') )

#id=divid的div标签下第1个span的id属性值
# print( bsp.select('div[id=divid] span')[0].attrs['id'] )

# 获得所有a元素的href属性集合
# print( [a.attrs['href'] for a in bsp.select('a')] )

# 所有属性【非空】的div元素集合列表
# print( [div for div in bsp.select('div') if div.attrs] )

# 所有属性为【空】的div元素集合列表
# print( [div fordivin bsp.select('div') if not div.attrs] )
