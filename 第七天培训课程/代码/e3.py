#coding:utf-8
try:
    a = 2
    b = 0
    print(a/b)
except:
    print('出错了！')
print('---------')
#可以使用else子句
a = 0
b = 1
try:
    c = b/a 
    print(c)
except ZeroDivisionError as a:
    print(a)
else:
    print('no error')
    