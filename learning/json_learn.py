import json

dic = {'name': 'laozi'}
#字符串必须是双引号""
i = 8
s = '123123'
data = json.dumps(dic)
data1 = json.dumps(i)
data2 = json.dumps(s)
lists = [123, 234]
data3 = json.dumps(lists)
print(data)
print(type(data))
# print(data1)
# print(type(data1))
# print(data2)
# print(type(data2))
# print(data3)
# print(type(data3))

with open( "111", "w" ) as f:
    f.write(data)
    # f.write(data1)
    # f.write(data2)
    # f.write(data3)

with open( "111", "r" ) as fr:
    data4 = json.loads( fr.read() )
    print(type(data4))
    print( data4 )