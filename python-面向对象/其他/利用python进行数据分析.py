from pandas import Series,DataFrame
import pandas as pd
import numpy as np

data={'state':['Ohio','Ohio','Ohio','Nevada','Nevada'],
      'year':[2000,2001,2002,2001,2002],
      'pop':[1.5,1.7,3.6,2.4,2.9]}

frame=DataFrame(data)
print(frame)
print("---------------------------------")

# 指定列序列，DataFrame的列就会按照指定顺序进行排列
frame2=DataFrame(data,columns=['year','state','pop'])
print(frame2)
print("---------------------------------")
# 原数据结构，不会发生变化
print(DataFrame(data))
print("---------------------------------")

# 跟Series一样，如果传入的列在数据中找不到，就会产生NA值
# 只有列名，没有对应值时，为NaN
frame3=DataFrame(data,columns=['year','state','pop','debt'],
                 index=['one','two','three','four','five'])

print(frame3)
# 显示每行索引的名字
print(frame3.index)
# 显示每列的列名
print(frame3.columns)
print("---------------------------------")

# 通过类似于字典标记的方式或属性的方式
# 可以将DataFrame的列获取为一个Series
print(frame3['state'])
print(frame3.year)
print("---------------------------------")

# 行也可以通过位置或名称的方式来进行获取。
# 由行获取
print(frame3.ix['three'])
print(frame3.ix[1])
print("=================================")
# 列可以通过赋值的方式进行修改。
# 如下，我们可以给空的”debt“列赋值一个标量或一组值
# 标量
frame3['debt']=16.5
print(frame3)
print("----------------")
# 数组
frame3['debt']=np.arange(5.)
print(frame3)

print("---------------------------------")
# 将列表或数组赋值给某个列的时候，其长度必须要跟DataFrame的长度向匹配。
#  如果赋值的是一个个Series ，就会精确的匹配DataFrame的索引，所有的空位都将被填上的缺失值。
val=Series([-1.2,-1.5,-1.7],index=['two','four','five'])
frame3['debt']=val
print(frame3)

# 为不存在的列赋值会创建一个新列。
frame3['eastern']=frame3.state=='Ohio'
print(frame3)
# 关键字del用于删除列
del frame3['eastern']
# 显示列名
print(frame3.columns)
print('-------------')
print(frame3['pop'])

print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
# 另一种常见的数据形式是嵌套字典（也就是字典的字典）
pop={'Nevada':{2001:2.4,2002:2.9},
     'Ohio':{2000:1.5,2001:1.7,2002:3.6}
     }

# 将它传给DataFrame，就会被解释为：
# 外层字典的键作为列，内层键作为行索引。
frame3=DataFrame(pop)
print(frame3)
print("---------")
# 对结果进行转置
print(frame3.T)
print("----------------------------")

# 内层字典的键会被合并、排序以及形成最终的索引。
# 若指定了显式索引，则不会这样
print(frame3)
#print(DataFrame(pop,index=[2000,2001,2002,2003]))

print('-------------')
# 由Series组成的字典差不多也是一样的用法
print(frame3)
print("----&&&&----")
pdata={'Ohio':frame3['Ohio'][:-2],
       'Nevada':frame3['Nevada'][:2]}
# 对于缺少的行列，自动补齐
print(DataFrame(pdata))
print("-------------------------")
# 如果设置了Data.Frame的index属性和columns的name属性
frame3.index.name='year'
frame3.columns.name='state'
print(frame3)
print("-------------------------")
# 以二维 ndarray的形式返回DataFrame的数据
print(frame3.values)
print(frame2.values)
