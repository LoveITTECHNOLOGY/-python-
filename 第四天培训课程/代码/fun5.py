#coding:utf-8
#位置参数 默认参数  
def fun1(a,b,sex='男'):
    print(a)
    print(sex)
#fun1(1,2)
'''
默认参数不可以在位置参数之前
def fun2(a,sex='男',b):
    print(a)
    print(sex)
fun2(1,2)
'''
#默认参数要放在元组参数后面
'''
def fun3(a,b,sex='男',*tup):
    print(a,b)   #100,200
    print(sex)   #1
    print(tup)   #2,3,4,5
fun3(100,200,1,2,3,4,5)
'''
def fun3(a,b,*tup,sex='男'):
    print(a,b)   #100,200
    print(sex)   #1
    print(tup)   #2,3,4,5
#fun3(100,200,1,2,3,4,5)
#位置参数  元组参数  默认  字典参数
def fun4(a,b,*tup,sex='男',**dic):
    print(dic)
    print(sex)
fun4(100,200,1,2,3,4,name='tyy',height='181cm',sex='女')
