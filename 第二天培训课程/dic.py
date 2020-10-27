#coding:utf-8
'''
字典，通过键值对的形式存储数据
key-value
key值必须使用不可变类型
dic = {key:value,key:value}
'''
dic1 = {'name':'tyy','age':30,'height':'181cm'}
print(dic1['name'])
dic2 = {}  #声明一个空字典
dic2[10]='abc'   #为字典添加数据
print(dic2[10])
#修改value值
dic1['age'] = 18
print(dic1)
#得到全部的key值
print(dic1.keys())
#得到全部的value值
print(dic1.values())
for i in dic1:
    print(i,dic1[i])