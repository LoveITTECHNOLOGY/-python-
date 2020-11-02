#coding:utf-8
#动态参数
#a接收一个参数，剩下的参数*形成一个元组
def add(a,*tup):  #实现若干个参数的加法运算
    c=0
    for i in tup: #遍历剩下的参数形成的元组
        c=c+i
    return c+a
#print(add(1,2,3,4,5,6,7,8,9,10))
#还可以接收多个关键字参数，形成字典
def test1(name,age=18,**dic):
    print(name)
    print(age)
    print(dic)
#test1('tyy',sex='M',height='181cm',a='b')
#混搭用法 tup前不能有默认参数
def test2(name,age,*tup,**dic):
    print(name)
    print(age)
    print(tup)
    print(dic)
test2('tyy',20,'qwrwer','12fe',sex='M',height='181cm')
#会把元组中的一个参数赋值给默认参数