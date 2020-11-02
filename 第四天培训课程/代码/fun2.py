#coding:utf-8
#普通参数 
def add(a,b):
    print(a+b)
#add(5,6) #普通参数的参数列表要对应 多了少了都会报错
#默认参数  
def add2(a,b=2):  #在定义函数时给形参赋值,解决方法的重载问题
    print(a+b)
add2(5,2)
#还可以传入指定的参数
def min(a,b):
    print(a-b)
#min(b=5,a=2)
