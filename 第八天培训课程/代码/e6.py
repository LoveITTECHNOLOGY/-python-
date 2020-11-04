#coding:utf-8
'''
让用户输入一个值，如果是字符串，直接输出
如果是数字，则乘以2再输出
！！！用户输入的都是字符串，从页面中获取的数据都是字符串
isinstance(obj,Class)判断obj是否是Class
isinstance(int(str),int) 判断obj是否是整型
'''
str = input('请输入一个字符串')
'''
if isinstance(int(str),int):
    print(int(str)*2)
else:
    print(str)
'''
try:
    print(int(str)*2)
except ValueError as e:
    print(e)
    print(str)