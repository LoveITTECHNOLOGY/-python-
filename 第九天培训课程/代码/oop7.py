#coding:utf-8
'''
方法的重写：父类的方法无法满足子类的需要，子类可以重写父类的方法
Python可以多继承
'''
class ClassSupA():
    def printSelf(self):
        print('SupA的方法')
class ClassA(ClassSupA):
    def printSelf(self):
        #重写了父类的方法
        print('A的方法')
class ClassB:
    def printSelf(self):
        print('B的方法')
class ClassC(ClassB,ClassA):
    pass
a = ClassA()
b = ClassB()
c = ClassC()
#继承多个类，方法一样，会调用先继承的
c.printSelf()
#issubclass(ClassA,ClassB)判断一个类是否是另一个类的子类
print(issubclass(ClassA,ClassSupA))
#isinstance(obj,Class) 判断一个对象是否是一个类的实例
print(isinstance(c,ClassSupA))