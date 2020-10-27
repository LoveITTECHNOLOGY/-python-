#coding:utf-8
'''
int float boolean complex(复数)
python只有一种整型，就是int
'''
a = 1  
print(id(a)) #id() 获取唯一标识变量的方法
print(type(a)) #type() 查看变量的数据类型
b = 3.14
#  del 变量名   , 可以删除变量
#del b
print(b)
#boolean True = 1,False = 0
#true和false是关键字，同时也是0和1，可以做运算
c = True
if c:
    print(a+c)
d = 4 + 3j  #复数
print(type(d))
a = 2
print(id(a))