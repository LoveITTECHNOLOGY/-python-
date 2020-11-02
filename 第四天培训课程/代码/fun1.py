#coding:utf-8
def add(a,b):  #a,b为形参,有返回值的方法
    c = a+b 
    return c   #c为返回值
#方法的调用
d = add(1,2)  #1,2为实参
print('结果为',d)
def add2(a,b):
    c = a+b 
    print(c)  #没有返回值，具体做的事情在函数中实现
