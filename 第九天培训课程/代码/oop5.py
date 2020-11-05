#coding:utf-8
class Test:
    stuCount = 0#类变量
    #类方法
    @classmethod
    def printCount(cls): #cls代指当前的类
        print('学生总人数为:%d' %Test.stuCount)
    @classmethod
    def fun1(cls): #以cls作为默认参数
        return '类方法'
    #静态方法
    @staticmethod
    def fun2():  #不需要放默认参数
        return '静态方法'
    #普通方法
    def fun3(self): #以self作为默认参数
        return '普通方法'
print(Test.fun1)
print(Test.fun2)
print(Test.fun3)
t1 = Test()
t2 = Test()
print(t1.fun1)
print(t1.fun2)
print(t1.fun3)
print(t2.fun1)
print(t2.fun2)
print(t2.fun3)