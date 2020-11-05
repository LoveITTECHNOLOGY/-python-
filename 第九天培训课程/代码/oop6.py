#coding:utf-8
class Parent:
    '定义一个父类'
    parentAttr = 100
    def __init__(self):
        print('调用父类的构造函数')
    def parentFun(self):
        print('调用父类的普通方法')
    def setAttr(self,value):
        Parent.parentAttr = value
    def getAttr(self):
        print('父类属性:%d' %Parent.parentAttr)
class Child(Parent):
    def __init__(self):
        #调用父类的构造方法，要显式调用
        Parent.__init__(self) 
        print('调用子类的构造方法')
    def childFun(self):
        print('调用子类的普通方法')
c = Child() #实例化一个子类
c.childFun() #调用子类的方法    
c.parentFun() #调用父类的方法
c.setAttr(300)
c.getAttr()